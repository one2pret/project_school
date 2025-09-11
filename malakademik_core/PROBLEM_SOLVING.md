# MalAkademik Core — Install Error Fix (RPC_ERROR)

Date: 2025-09-10

## Issue
- Installing `malakademik_core` failed with:
  - `ValueError: External ID not found in the system: malakademik_core.action_malakademik_student`.
  - ParseError reported at `views/menus.xml` on a `<menuitem>` that references `action_malakademik_student`.

## Root Cause
- In `__manifest__.py`, `views/menus.xml` loaded before the view/action XML files.
- Menu items reference actions by XML ID; when menus load first, those actions don’t exist yet, causing missing external ID errors.

## Fix
- Reordered manifest so actions load before menus.
  - Moved `views/menus.xml` to the end of the `data` list` (__manifest__.py).
- Use the simpler, proven pattern like in `penilaian_kinerja_dosen`:
  - Link actions directly on `<menuitem action="action_xmlid" .../>`.
  - Ensure action records are defined before menus (manifest order).
  - File: `workspace_dev/project_school/malakademik_core/views/menus.xml`.

## Affected Files
- `workspace_dev/project_school/malakademik_core/__manifest__.py`
- `workspace_dev/project_school/malakademik_core/views/menus.xml` (no content changes, but depends on actions)

## Validation Steps
1. Update App List and install `MalAkademik Core`.
2. Verify no errors during module installation.
3. Open menus under `Academics` and confirm they open the corresponding list views.
4. If demo data is enabled, confirm sample records are visible.

## Notes
- All list/form views use the new `<list>` view type (Odoo 18).
- Indonesian translations available in `i18n/id.po`.
