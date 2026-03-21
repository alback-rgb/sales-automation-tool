from datetime import datetime, timedelta

def process_data(df):
    # אם אין תאריך — fallback למצב הישן
    if "date" not in df.columns:
        grouped = df.groupby("product_name")["quantity"].sum()
        top = grouped.sort_values(ascending=False).head(5)
        low = grouped.sort_values().head(5)

        return {
            "top": top,
            "low": low,
            "insights": ["אין נתוני תאריך להשוואה"]
        }

    # חישוב שבוע נוכחי ושבוע קודם
    latest_date = df["date"].max()

    this_week_start = latest_date - timedelta(days=7)
    last_week_start = latest_date - timedelta(days=14)

    this_week = df[df["date"] >= this_week_start]
    last_week = df[(df["date"] >= last_week_start) & (df["date"] < this_week_start)]

    # Top / Low
    grouped = this_week.groupby("product_name")["quantity"].sum()

    top = grouped.sort_values(ascending=False).head(5)
    low = grouped.sort_values().head(5)

    # סיכום כללי
    this_total = this_week["quantity"].sum()
    last_total = last_week["quantity"].sum()

    # שינוי באחוזים
    change_percent = 0
    if last_total > 0:
        change_percent = ((this_total - last_total) / last_total) * 100

    # פילוח קטגוריות (אם קיים)
    category_summary = None
    if "category" in df.columns:
        category_summary = this_week.groupby("category")["quantity"].sum().sort_values(ascending=False)

    # תובנות
    insights = []

    if change_percent > 0:
        insights.append(f"📈 עלייה של {change_percent:.1f}% במכירות")
    elif change_percent < 0:
        insights.append(f"📉 ירידה של {abs(change_percent):.1f}% במכירות")

    if not top.empty:
        insights.append(f"🔥 המוצר המוביל: {top.index[0]}")

    if not low.empty:
        insights.append(f"⚠️ מוצר חלש: {low.index[0]}")

    return {
        "top": top,
        "low": low,
        "category_summary": category_summary,
        "change_percent": change_percent,
        "insights": insights
    }