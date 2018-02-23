#-*- coding: utf-8 -*-
from openerp import models, fields, api

class Aplicacionejemplo01Task(models.Model):
    _name = 'aplicacionejemplo01.task'
    name = fields.Char('Incidencia', required=True)
    name2 = fields.Char('Observaciones', required=True)
    name3 = fields.Char('Fecha', required=True)
    tlfno = fields.Char('Telefono encargado', required=True)
    email = fields.Char('Email encargado', required=True)
    comboBo = fields.Selection([('Grave','Grave'),('Intermedio','Intermedio'),('Bajo','Bajo')],string='Nivel de incidencia',required=True)
    prioridad = fields.Selection([('1','bajo'),('2','normal'),('3','alto'),('4','muy alto')],'prioridad')
    name4 = fields.Char('Imagen', help='Selecciona la imagen de la incidencia')
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)

    @api.one  
    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True

    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True
