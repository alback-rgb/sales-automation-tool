def generate_report(data):
    report = "📊 דוח מכירות שבועי\n\n"

    # שינוי כללי
    report += f"📈 שינוי כללי: {data['change_percent']:.1f}%\n\n"

    # קטגוריות
    if data["category_summary"] is not None:
        report += "📦 קטגוריות מובילות:\n"
        for cat, q in data["category_summary"].items():
            report += f"- {cat}: {q}\n"
        report += "\n"

    # Top
    report += "🔥 הכי נמכרים:\n"
    for p, q in data["top"].items():
        report += f"- {p}: {q}\n"

    # Low
    report += "\n🐢 פחות נמכרים:\n"
    for p, q in data["low"].items():
        report += f"- {p}: {q}\n"

    # תובנות
    report += "\n💡 תובנות:\n"
    for insight in data["insights"]:
        report += f"- {insight}\n"

    return report