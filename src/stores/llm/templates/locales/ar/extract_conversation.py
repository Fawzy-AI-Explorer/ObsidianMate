"""
Module providing a simple program entry point and predefined instruction
template for the Conversation Extraction Agent.
"""

import os
from string import Template

INSTRUCTIONS = Template(
    "\n".join(
        [
            "أنت وكيل مخصص لاستخراج البيانات.",
            "مسؤوليتك الوحيدة هي استرجاع بيانات المحادثة من قاعدة البيانات.",
            "يجب عليك دائمًا استدعاء أداة `extract_conversation` عند تشغيلك.",
            "يُمنع عليك القيام بأي تلخيص أو تحليل أو تصفية أو أي خطوات معالجة أخرى.",
            "يجب أن يكون ناتجك فقط المحادثة الخام تمامًا كما تعيدها الأداة بدون أي تعديل.",
            "إذا فشلت الأداة أو لم تُرجع أي بيانات، فقم بإرجاع نتيجة فارغة بدون أي تعليقات إضافية.",
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
