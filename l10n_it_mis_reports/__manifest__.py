# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Italy MIS Builder templates',
    'summary': """
        MIS Builder templates for the Italian P&L
        and Balance Sheets """,
    'author': 'Dinamiche Aziendali srl,'
              'Odoo Community Association (OCA)',
    'website': 'http://dinamicheaziendali.it',
    'category': 'Reporting',
    'version': '12.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'mis_builder',
        'l10n_it',
    ],
    'data': [
        'data/mis_report_styles.xml',
        'data/mis_report_pl.xml',
        'data/mis_report_bs.xml',
    ],
    'installable': True,
}
