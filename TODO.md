# TODO

- [x] Inspect sidebar and app page rendering flow.
- [x] Move page rendering out of `with st.sidebar:` by making `render_sidebar()` UI-only.
- [x] Add `render_page_for_sidebar_selection()` to render the selected page in the main content area.
- [x] Update `ui/pages.py` to call `render_page_for_sidebar_selection()` after `render_sidebar()`.
- [x] Sanity-check Python syntax with `py_compile`.

