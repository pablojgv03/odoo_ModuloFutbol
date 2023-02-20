# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class futbol(models.Model):
#     _name = 'futbol.futbol'
#     _description = 'futbol.futbol'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api

class jugador(models.Model):
  _name = 'futbol.jugador'
  _description = 'Jugador'

  nombre = fields.Char(string='Nombre',required=True)
  numero = fields.Integer(string='Numero',required=True)


  #relaciones
  equipo_id = fields.Many2one('futbol.equipo',string='Equipo')



class equipo(models.Model):
  _name = 'futbol.equipo'
  _description = 'equipo'


  nombre = fields.Char(string='Nombre',required=True)
  division = fields.Char(string='Division',required=True)

  # relaciones
  jugador_id = fields.One2many('futbol.jugador', 'equipo_id',string='Jugador')
  
  ciudad_id = fields.Many2one('futbol.ciudad', string='Ciudad')

  entrenador_id = fields.One2many('futbol.entrenador', 'equipo_id',string='Entrenador')

class entrenador(models.Model):
  _name = 'futbol.entrenador'
  _description = 'entrenador'

  nombre = fields.Char(string='Nombre',required=True)

  #relaciones
  equipo_id = fields.Many2one('futbol.equipo', string='Equipo')
    


class ciudad(models.Model):
  _name = 'futbol.ciudad'
  _description = 'ciudad'

  nombre = fields.Char(string='Nombre',required=True)
  pais = fields.Char(string='Pais',required=True)
  # relaciones

  equipo_id = fields.One2many('futbol.equipo', 'ciudad_id', string='Equipo')