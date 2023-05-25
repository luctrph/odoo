from odoo import fields, models


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Boook Manager'
    _order = 'date_release desc, name'
    _rec_name = 'short_name'
    name = fields.Char(string='Title', required=True)
    short_name = fields.Char('Short Title', translate=True, index=True)
    notes = fields.Text('Internal Notes')
    state = fields.Selection([('draft', 'Not Available'), ('available', 'Available'), ('lost', 'Lost')], 'State',
                             default='draft')
    description = fields.Html('Description', sanitize=True, strip_stype=True)
    cover = fields.Binary('Book Cover')
    out_of_print = fields.Boolean('Out of Print?')
    date_release = fields.Date('Release Date')
    date_updated = fields.Datetime('Last Updated')
    pages = fields.Integer('Number of Pages',
                           group='base.group_user',
                           states={'lost': [('readonly', True)]},
                           help='Total book pages count', company_dependent=False)
    reader_rating = fields.Float(
        'Reader Average Rating', digits=(14, 3),  # Optional precision decimals
    )

    author_ids = fields.Many2many(
        'res.partner', string='Authors'
    )
    currency_id = fields.Many2one('res.currency', string='Currency')
    retail_price = fields.Monetary(
        'Retail Price',
        # optional: currency_field='currency_id',
    )
    active = fields.Boolean('Active', default=True)


def name_get(self):
    result = []
    for record in self:
        rec_name = "%s ---(%s)" % (record.name, record.date_release)
        result.append((record.id, rec_name))
    return result
