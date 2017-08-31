import os

from openfisca_core.taxbenefitsystems import TaxBenefitSystem
from .entities import entities

COUNTRY_DIR = os.path.dirname(os.path.abspath(__file__))


class SpainTaxBenefitSystem(TaxBenefitSystem):
    def __init__(self):
        TaxBenefitSystem.__init__(self, entities)

        # We add to our tax and benefit system all the variables
        self.add_variables_from_directory(os.path.join(COUNTRY_DIR, 'variables'))

        # We add to our tax and benefit system all the legislation parameters defined in the  parameters files
        param_files = [
            '__root__.xml',
        ]

        for param_file in param_files:
            param_path = os.path.join(COUNTRY_DIR, 'parameters', param_file)
            self.add_legislation_params(param_path)
