# from wtforms import (
#     SelectField,
# )
# from app.models import (
#     Cliente,
#     Producto,
#     Estado,
#     Regimen,
#     CodigoProducto,
#     UnidadProducto,
#     MetodoPago,
#     FormaPago,
# )
# from wtforms.widgets import html_params, Select
# from markupsafe import Markup


# class ClienteModalSelect(Select):
#     def __call__(self, field, **kwargs):
#         kwargs.setdefault("id", field.id)
#         html = []
#         invalid = ""
#         invalid_feedback = ""
#         if field.errors:
#             invalid = "is-invalid"
#             invalid_feedback += '<div class="invalid-feedback">'
#             for error in field.errors:
#                 invalid_feedback += f"<span>{error}</span>"
#             invalid_feedback += "</div>"
#         html.append(
#             f"""
#             <div class="input-group mb-3">
#                 <span class="input-group-text">Cliente</span>
#                 <input type="text" placeholder="{field.label.text}" class="disabled form-control {invalid}" tabindex="-1">
#                 <span class="input-group-text"><i class="bi bi-search" role="button" data-bs-toggle="modal" data-bs-target="#modal{field.id}" ></i></span>
#                 {invalid_feedback}
#             </div>


#                 <div class="modal" tabindex="-1" role="dialog" aria-hidden="true" data-keyboard="false" data-backdrop="static" id="modal{field.id}">
#                 <div class="modal-dialog modal-lg">
#                     <div class="modal-content">
#                         <div class="modal-header">
#                             <h1 class="modal-title fs-5 text-center" >{field.label.text}</h1>
#                             <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Cerrar"></button>
#                         </div>

#                         <div class="modal-body">
#                             <table class="table modal-table">
#                                 <thead class="table-light">
#                                     <tr>
#                                         <th>Seleccionar</th>
#                                         <th>ID</th>
#                                         <th>Nombre</th>
#                                         <th>RFC</th>
#                                     </tr>
#                                 </thead>
#                                 <tbody>
#         """
#         )
#         for val, persona, selected, _ in field.iter_choices():
#             html.append(
#                 f"""

#                      <tr class=""
#                                             data-dismiss="modal"
#                                             data-nombre="">
#                                             <td><input id="{field.id}-{val}" data-bs-dismiss="modal" value="{val}"  data-label="{persona.nombre} {persona.paterno} {persona.materno}" type="radio" {html_params(name=field.name, value=val, checked=selected)}></td>
#                                             <td>{val}</td>
#                                             <td style='white-space:normal'>{persona.nombre} {persona.paterno} {persona.materno}</td>
#                                             <td>{persona.rfc}</td>
#                                         </tr>
#         """
#             )

#         html.append(
#             """
#                                 </tbody>
#                             </table>
#                             <div class="row">&nbsp;</div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#         """
#         )
#         return Markup(" ".join(html))


# class ClienteField(SelectField):
#     widget = ClienteModalSelect()

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.choices = []  # Initialize empty to avoid None

#     def iter_choices(self):
#         clientes = [(c.id, c.persona) for c in Cliente.query.all()]
#         for value, persona in clientes:
#             yield (value, persona, self.coerce(value) == self.data, {})

#     def pre_validate(self, form):
#         # Skip the parent class validation since we load dynamically
#         clientes = [(c.id, c.persona) for c in Cliente.query.all()]
#         valid_values = {value for value, _ in clientes}
#         if self.data not in valid_values:
#             self.errors.append("Selecciona una opción válida")


# class ProductoField(SelectField):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.choices = []  # Initialize empty to avoid None

#     def iter_choices(self):
#         productos = [(p.id, p.nombre) for p in Producto.query.all()]
#         for value, label in productos:
#             yield (value, label, self.coerce(value) == self.data, {})

#     def pre_validate(self, form):
#         # Skip the parent class validation since we load dynamically
#         productos = [(p.id, p.nombre) for p in Producto.query.all()]
#         valid_values = {value for value, _ in productos}
#         if self.data not in valid_values:
#             self.errors.append("Selecciona una opción válida")


# class EstadoField(SelectField):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.choices = []  # Initialize empty to avoid None

#     def iter_choices(self):
#         estados = [(e.id, e.nombre) for e in Estado.query.all()]
#         for value, label in estados:
#             yield (value, label, self.coerce(value) == self.data, {})

#     def pre_validate(self, form):
#         # Skip the parent class validation since we load dynamically
#         estados = [(e.id, e.nombre) for e in Estado.query.all()]
#         valid_values = {value for value, _ in estados}
#         if self.data not in valid_values:
#             self.errors.append("Selecciona una opción válida")


# class RegimenField(SelectField):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.choices = []  # Initialize empty to avoid None

#     def iter_choices(self):
#         regimenes = [(r.id, f"{r.id} {r.descripcion}") for r in Regimen.query.all()]
#         for value, label in regimenes:
#             yield (value, label, self.coerce(value) == self.data, {})

#     def pre_validate(self, form):
#         # Skip the parent class validation since we load dynamically
#         regimenes = [(r.id, f"{r.id} {r.descripcion}") for r in Regimen.query.all()]
#         valid_values = {value for value, _ in regimenes}
#         if self.data not in valid_values:
#             self.errors.append("Selecciona una opción válida")


# class CodigoProductoField(SelectField):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.choices = []  # Initialize empty to avoid None

#     def iter_choices(self):
#         codigos = [(c.id, f"{c.codigo} {c.nombre}") for c in CodigoProducto.query.all()]
#         for value, label in codigos:
#             yield (value, label, self.coerce(value) == self.data, {})

#     def pre_validate(self, form):
#         # Skip the parent class validation since we load dynamically
#         codigos = [(c.id, f"{c.codigo} {c.nombre}") for c in CodigoProducto.query.all()]
#         valid_values = {value for value, _ in codigos}
#         if self.data not in valid_values:
#             self.errors.append("Selecciona una opción válida")


# class UnidadProductoField(SelectField):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.choices = []  # Initialize empty to avoid None

#     def iter_choices(self):
#         unidades = [
#             (u.id, f"{u.codigo} {u.nombre}") for u in UnidadProducto.query.all()
#         ]
#         for value, label in unidades:
#             yield (value, label, self.coerce(value) == self.data, {})

#     def pre_validate(self, form):
#         # Skip the parent class validation since we load dynamically
#         unidades = [
#             (u.id, f"{u.codigo} {u.nombre}") for u in UnidadProducto.query.all()
#         ]
#         valid_values = {value for value, _ in unidades}
#         if self.data not in valid_values:
#             self.errors.append("Selecciona una opción válida")


# class MetodoPagoField(SelectField):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.choices = []  # Initialize empty to avoid None

#     def iter_choices(self):
#         metodos = [
#             (m.id, f"{m.codigo} {m.descripcion}") for m in MetodoPago.query.all()
#         ]
#         for value, label in metodos:
#             yield (value, label, self.coerce(value) == self.data, {})

#     def pre_validate(self, form):
#         # Skip the parent class validation since we load dynamically
#         metodos = [
#             (m.id, f"{m.codigo} {m.descripcion}") for m in MetodoPago.query.all()
#         ]
#         valid_values = {value for value, _ in metodos}
#         if self.data not in valid_values:
#             self.errors.append("Selecciona una opción válida")


# class FormaPagoField(SelectField):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.choices = []  # Initialize empty to avoid None

#     def iter_choices(self):
#         formas = [(f.id, f"{f.id} {f.descripcion}") for f in FormaPago.query.all()]
#         for value, label in formas:
#             yield (value, label, self.coerce(value) == self.data, {})

#     def pre_validate(self, form):
#         # Skip the parent class validation since we load dynamically
#         formas = [(f.id, f"{f.id} {f.descripcion}") for f in FormaPago.query.all()]
#         valid_values = {value for value, _ in formas}
#         if self.data not in valid_values:
#             self.errors.append("Selecciona una opción válida")
