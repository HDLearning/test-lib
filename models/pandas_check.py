import logging

_logger = logging.getLogger(__name__)

try:
    import pandas as pd
    df = pd.DataFrame({"Test": [1, 2, 3]})
    _logger.info("Pandas is installed and working: %s", df)
except ImportError:
    _logger.error("Pandas is NOT installed!")
