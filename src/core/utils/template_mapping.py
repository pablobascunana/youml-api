import datetime
import os

template_mapping = {
    "ACTUAL_YEAR": str(datetime.date.today().year),
    "URL_VERIFICATION_ENDPOINT": f"{os.environ.get('URL_VERIFICATION_ENDPOINT')}?"
                                 f"token=##VERIFICATION_TOKEN##",
}
