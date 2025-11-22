"""Markdown Template - Arabic Locales."""
import os
from string import Template

INSTRUCTIONS = Template(
    "\n".join(
        [
            "أنت مساعد مفيد يقوم بتحويل نص المستخدم إلى تنسيق ماركداون.",
            "تأكد من أن صياغة الماركداون صحيحة وأن المحتوى منظم بشكل جيد.",
            "لا تتضمن أي تفسيرات أو نصوص إضافية خارج محتوى الماركداون.",
            "استخدم عناصر الماركداون المناسبة مثل العناوين، القوائم، الروابط، الصور، كتل الشيفرة، إلخ، بناءً على سياق النص.",
        ]
    )
)

def main():
    """Entry Point for the Program."""
    print(
        f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module. Nothing to do ^_____^!"
    )


if __name__ == "__main__":
    main()
