from data_loader import load_sales_data
from email_sender import send_email

file_path = "דוח 15 למרץ עד 20 למרץ.xls"

try:
    sales_data = load_sales_data(file_path)

    # יצירת דוח מלא
    report = "סיכום מכירות מלא:\n\n"

    for product, qty in sales_data.items():
        report += f"{product}: {int(qty)}\n"

    # שליחת מייל
    send_email(report)

    print("✅ הדוח המלא נשלח בהצלחה!")

except Exception as e:
    print("\n❌ שגיאה:")
    print(e)