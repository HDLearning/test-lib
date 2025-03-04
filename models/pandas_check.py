from odoo import models, api
from odoo.exceptions import UserError

class PandasCheck(models.Model):
    _name = "pandas.check"
    _description = "Check if Pandas is Installed"

    @api.model
    def check_pandas(self):
        try:
            import pandas as pd
            df = pd.DataFrame({"Test": [1, 2, 3]})
            return {"message": f"Pandas is installed and working: {df.to_string()}"}
        except ImportError:
            raise UserError("Pandas is NOT installed! Please install it using 'pip install pandas'.")
