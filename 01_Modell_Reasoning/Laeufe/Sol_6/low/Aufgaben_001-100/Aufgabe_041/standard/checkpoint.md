# Checkpoint

Consolidated List methods in core.models.List and removed ListMixin.
Added list and changeset registration in core.lists.model.register_models.
Updated plugin list type annotation to List.
Core list tests pass; plugin list suite has one unrelated web.ctx.env fixture failure; list API suite cannot collect because cookielib is unavailable.
Focused owner and registration checks pass.
