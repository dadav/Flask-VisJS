import pytest
from flask import render_template_string
from flask_visjs import Network


@pytest.mark.usefixtures('client')
class TestVisJSConfiguration:
    def test_local_serving_is_off(self, app):
        app.config['VISJS_SERVE_LOCAL'] = False
        rendered = render_template_string('{{ net.inject_css() }}{{ net.inject_js() }}', net=Network())
        cdn = app.config['VISJS_CDN_TEMPLATE']
        version = app.config['VISJS_VERSION']
        css_filename = app.config['VISJS_CSS_FILENAME']
        js_filename = app.config['VISJS_JS_FILENAME']
        cdn_css = cdn.format(VERSION=version, FILENAME=css_filename)
        cdn_js = cdn.format(VERSION=version, FILENAME=js_filename)
        assert cdn_css in rendered
        assert cdn_js in rendered

    def test_local_serving_is_on(self, app):
        app.config['VISJS_SERVE_LOCAL'] = True
        rendered = render_template_string('{{ net.inject_css() }}{{ net.inject_js() }}', net=Network())
        cdn = app.config['VISJS_CDN_TEMPLATE']
        version = app.config['VISJS_VERSION']
        css_filename = app.config['VISJS_CSS_FILENAME']
        js_filename = app.config['VISJS_JS_FILENAME']
        cdn_css = cdn.format(VERSION=version, FILENAME=css_filename)
        cdn_js = cdn.format(VERSION=version, FILENAME=js_filename)
        assert cdn_css not in rendered
        assert cdn_js not in rendered

    def test_use_another_version(self, app):
        app.config['VISJS_SERVE_LOCAL'] = False
        app.config['VISJS_VERSION'] = '1337'
        css_rendered = render_template_string('{{ net.inject_css() }}', net=Network())
        js_rendered = render_template_string('{{ net.inject_js() }}', net=Network())
        assert '1337' in css_rendered
        assert '1337' in js_rendered

    def test_use_another_cdn(self, app):
        custom_cdn = 'https://example.com/'
        app.config['VISJS_SERVE_LOCAL'] = False
        app.config['VISJS_CDN_TEMPLATE'] = custom_cdn
        css_rendered = render_template_string('{{ net.inject_css() }}', net=Network())
        js_rendered = render_template_string('{{ net.inject_js() }}', net=Network())
        assert custom_cdn in css_rendered
        assert custom_cdn in js_rendered

    def test_use_another_css_filename(self, app):
        custom_filename = 'foobar.css'
        app.config['VISJS_SERVE_LOCAL'] = False
        app.config['VISJS_CSS_FILENAME'] = custom_filename
        css_rendered = render_template_string('{{ net.inject_css() }}', net=Network())
        assert custom_filename in css_rendered

    def test_use_another_js_filename(self, app):
        custom_filename = 'foobar.js'
        app.config['VISJS_SERVE_LOCAL'] = False
        app.config['VISJS_JS_FILENAME'] = custom_filename
        js_rendered = render_template_string('{{ net.inject_js() }}', net=Network())
        assert custom_filename in js_rendered

    def test_use_another_graph_template(self, app, tmp_path):
        template_content = 'foobar'
        custom_template_path = tmp_path / 'my_template.html.j2'
        with open(custom_template_path, 'wt') as tmp_file:
            tmp_file.write(template_content)
        app.config['VISJS_CUSTOM_TEMPLATE_PATH'] = custom_template_path
        template_rendered = render_template_string('{{ net.inject_graph() }}', net=Network())
        assert template_content in template_rendered
