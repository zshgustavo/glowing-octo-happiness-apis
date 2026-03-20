from .ga4 import extract_ga4
from .tiktok import extract_tiktok
from .google_ads import extract_google_ads
from .dv360 import extract_dv360
from .x import extract_x

EXTRACTORS = {
    "ga4": extract_ga4,
    "tiktok": extract_tiktok,
    "google_ads": extract_google_ads,
    "dv360": extract_dv360,
    "x": extract_x,
}
