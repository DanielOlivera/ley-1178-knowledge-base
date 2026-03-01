# 🌟 Centro de Conocimiento — Cursos y Normativa

> Arquitectura estrella: múltiples bases de conocimiento independientes con un nodo central de consulta.

---

## 📚 Bases de Conocimiento

| # | Base de Conocimiento | Descripción | Estado |
|---|---------------------|-------------|--------|
| 1 | [kb_1178](kb_1178/) | Ley 1178 — Administración y Control Gubernamentales | ✅ Activa |
| 2 | [kb_PP](kb_PP/) | Políticas Públicas | ✅ Activa |

---

## 🏗️ Arquitectura

```
                    ┌──────────────┐
                    │  CONSULTANTE │
                    │   (Usuario)  │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │  CONSULTADO  │
                    │     (IA)     │
                    └──────┬───────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
    ┌─────▼─────┐    ┌─────▼─────┐    ┌─────▼─────┐
    │  KB 1     │    │  KB 2     │    │  KB N     │
    │ Ley 1178  │    │ (futuro)  │    │ (futuro)  │
    └───────────┘    └───────────┘    └───────────┘
```

**Regla:** Cada KB es independiente. Solo se hace consulta cruzada cuando se necesita información de múltiples bases.

---

## 📋 Convenciones

- Cada KB tiene su propia carpeta con `README.md`
- Los PDFs fuente van en `fuentes/` dentro de cada KB
- El contenido procesado (Markdown) va en carpetas temáticas
- Los exámenes y notas van en `examenes/` y `recursos/`
