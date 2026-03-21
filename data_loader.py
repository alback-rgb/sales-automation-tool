import pandas as pd

def load_sales_data(file_path):
    try:
        df = pd.read_excel(file_path)

        import sys
        sys.stdout.reconfigure(encoding='utf-8')

        print("עמודות בקובץ:")
        print(df.columns)

        # ניקוי עמודות ריקות
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        # זיהוי עמודת מוצר
        if 'שם מוצר' in df.columns:
            product_col = 'שם מוצר'
        elif 'תאור המוצר' in df.columns:
            product_col = 'תאור המוצר'
        else:
            raise Exception("❌ לא נמצאה עמודת מוצר")

        # זיהוי עמודת כמות
        if 'כמות' in df.columns:
            quantity_col = 'כמות'
        else:
            raise Exception("❌ לא נמצאה עמודת כמות")

        # ניקוי נתונים
        df = df[[product_col, quantity_col]].dropna()

        # המרה למספרים
        df[quantity_col] = pd.to_numeric(df[quantity_col], errors='coerce')
        df = df.dropna()

        # סיכום לפי מוצר
        summary = df.groupby(product_col)[quantity_col].sum()

        # מיון מהגבוה לנמוך (אבל בלי לחתוך!)
        summary = summary.sort_values(ascending=False)

        return summary  # ✅ מחזיר הכל

    except Exception as e:
        raise Exception(f"שגיאה בקריאת הקובץ: {e}")