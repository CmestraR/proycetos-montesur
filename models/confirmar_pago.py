from odoo import models, fields

class Credit(models.Model):
    _inherit = 'credit'  

    # Cambiar estado del objeto grafico 
    def boton_publicar(self):
        self.state = 'paid_out'
