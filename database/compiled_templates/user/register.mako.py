# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1500946389.258808
_enable_loop = True
_template_filename = 'templates/user/register.mako'
_template_uri = '/user/register.mako'
_source_encoding = 'ascii'
_exports = ['body', 'init', 'javascripts', 'center_panel', 'render_registration_form']



#This is a hack, we should restructure templates to avoid this.
def inherit(context):
    if context.get('trans').webapp.name == 'galaxy' and context.get( 'use_panels', True ):
        return '/webapps/galaxy/base_panels.mako'
    else:
        return '/base.mako'


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('__anon_0xb9ec350', context._clean_inheritance_tokens(), templateuri=u'/message.mako', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, '__anon_0xb9ec350')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, (inherit(context)), _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xb9ec350')._populate(_import_ns, [u'render_msg'])
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xb9ec350')._populate(_import_ns, [u'render_msg'])
        status = _import_ns.get('status', context.get('status', UNDEFINED))
        render_msg = _import_ns.get('render_msg', context.get('render_msg', UNDEFINED))
        redirect_url = _import_ns.get('redirect_url', context.get('redirect_url', UNDEFINED))
        cntrller = _import_ns.get('cntrller', context.get('cntrller', UNDEFINED))
        message = _import_ns.get('message', context.get('message', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        def render_registration_form(form_action=None):
            return render_render_registration_form(context,form_action)
        __M_writer = context.writer()
        __M_writer(u'\n    <div style="')
        __M_writer(unicode( 'margin: 1em;' if context.get( 'use_panels', True ) else '' ))
        __M_writer(u'">\n\n')
        if redirect_url:
            __M_writer(u'            <script type="text/javascript">\n                top.location.href = \'')
            __M_writer(filters.html_escape(unicode(redirect_url )))
            __M_writer(u"';\n            </script>\n")
        elif message:
            __M_writer(u'            ')
            __M_writer(unicode(render_msg( message, status )))
            __M_writer(u'\n')
        __M_writer(u'\n')
        if ( cntrller=='admin' and trans.user_is_admin() ) or not trans.user:
            __M_writer(u'            ')
            __M_writer(unicode(render_registration_form()))
            __M_writer(u'\n\n')
            if trans.app.config.get( 'terms_url', None ) is not None:
                __M_writer(u'                <br/>\n                <p>\n                    <a href="')
                __M_writer(unicode(trans.app.config.get('terms_url', None)))
                __M_writer(u'">Terms and Conditions for use of this service</a>\n                </p>\n')
        __M_writer(u'\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_init(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xb9ec350')._populate(_import_ns, [u'render_msg'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n')

        self.has_left_panel=False
        self.has_right_panel=False
        self.active_view="user"
        self.message_box_visible=False
        
        
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_javascripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xb9ec350')._populate(_import_ns, [u'render_msg'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(parent.javascripts()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_center_panel(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xb9ec350')._populate(_import_ns, [u'render_msg'])
        def body():
            return render_body(context)
        __M_writer = context.writer()
        __M_writer(u'\n    ')
        __M_writer(unicode(body()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_registration_form(context,form_action=None):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0xb9ec350')._populate(_import_ns, [u'render_msg'])
        username = _import_ns.get('username', context.get('username', UNDEFINED))
        redirect = _import_ns.get('redirect', context.get('redirect', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        registration_warning_message = _import_ns.get('registration_warning_message', context.get('registration_warning_message', UNDEFINED))
        subscribe_checked = _import_ns.get('subscribe_checked', context.get('subscribe_checked', UNDEFINED))
        t = _import_ns.get('t', context.get('t', UNDEFINED))
        cntrller = _import_ns.get('cntrller', context.get('cntrller', UNDEFINED))
        trans = _import_ns.get('trans', context.get('trans', UNDEFINED))
        email = _import_ns.get('email', context.get('email', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n    ')

        if form_action is None:
            form_action = h.url_for( controller='user', action='create', cntrller=cntrller )
        from galaxy.web.form_builder import CheckboxField
        subscribe_check_box = CheckboxField( 'subscribe' )
            
        
        __M_writer(u'\n\n    <script type="text/javascript">\n        $(document).ready(function() {\n\n            function validateString(test_string, type) {\n                var mail_re = /^(([^<>()[\\]\\\\.,;:\\s@\\"]+(\\.[^<>()[\\]\\\\.,;:\\s@\\"]+)*)|(\\".+\\"))@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\])|(([a-zA-Z\\-0-9]+\\.)+[a-zA-Z]{2,}))$/;\n                //var mail_re_RFC822 = /^([^\\x00-\\x20\\x22\\x28\\x29\\x2c\\x2e\\x3a-\\x3c\\x3e\\x40\\x5b-\\x5d\\x7f-\\xff]+|\\x22([^\\x0d\\x22\\x5c\\x80-\\xff]|\\x5c[\\x00-\\x7f])*\\x22)(\\x2e([^\\x00-\\x20\\x22\\x28\\x29\\x2c\\x2e\\x3a-\\x3c\\x3e\\x40\\x5b-\\x5d\\x7f-\\xff]+|\\x22([^\\x0d\\x22\\x5c\\x80-\\xff]|\\x5c[\\x00-\\x7f])*\\x22))*\\x40([^\\x00-\\x20\\x22\\x28\\x29\\x2c\\x2e\\x3a-\\x3c\\x3e\\x40\\x5b-\\x5d\\x7f-\\xff]+|\\x5b([^\\x0d\\x5b-\\x5d\\x80-\\xff]|\\x5c[\\x00-\\x7f])*\\x5d)(\\x2e([^\\x00-\\x20\\x22\\x28\\x29\\x2c\\x2e\\x3a-\\x3c\\x3e\\x40\\x5b-\\x5d\\x7f-\\xff]+|\\x5b([^\\x0d\\x5b-\\x5d\\x80-\\xff]|\\x5c[\\x00-\\x7f])*\\x5d))*$/;\n                var username_re = /^[a-z0-9._\\-]{3,255}$/;\n                if (type === \'email\') {\n                    return mail_re.test(test_string);\n                } else if (type === \'username\'){\n                    return username_re.test(test_string);\n                }\n            }\n\n            function renderError(message) {\n                if (!$(".errormessage").size()) {\n                    $(\'<div/>\').addClass(\'errormessage\').insertBefore(\'#registrationForm\');\n                }\n                console.debug( $( \'#registrationForm\' ) );\n                console.debug( \'.errormessage:\', $( \'.errormessage\' ) );\n                $(".errormessage").html(message);\n            }\n\n            $("[name=\'password\']").complexify({\'minimumChars\':6}, function(valid, complexity){\n                var progressBar = $(\'.progress-bar\');\n                var color = valid ? \'lightgreen\' : \'red\';\n\n                progressBar.css(\'background-color\', color);\n                progressBar.css({\'width\': complexity + \'%\'});\n            });\n\n            $(\'#registration\').bind(\'submit\', function(e) {\n                $(\'#send\').attr(\'disabled\', \'disabled\');\n\n                // we need this value to detect submitting at backend\n                var hidden_input = \'<input type="hidden" id="create_user_button" name="create_user_button" value="Submit"/>\';\n                $("#email_input").before(hidden_input);\n\n                var error_text_email = \'The format of the email address is not correct.\';\n                var error_text_email_long = \'Email address cannot be more than 255 characters in length.\';\n                var error_text_username_characters = "Public name must contain only lowercase letters, numbers, \'.\', \'_\' and \'-\'. It also has to be between 3 and 255 characters in length.";\n                var error_text_password_short = \'Use a password of at least 6 characters\';\n                var error_text_password_match = "Passwords don\'t match";\n\n                var validForm = true;\n\n                var email = $(\'#email_input\').val();\n                var name = $(\'#name_input\').val();\n                if (email.length > 255){ renderError(error_text_email_long); validForm = false;}\n                else if (!validateString(email,"email")){ renderError(error_text_email); validForm = false;}\n                else if (!($(\'#password_input\').val() === $(\'#password_check_input\').val())){ renderError(error_text_password_match); validForm = false;}\n                else if ($(\'#password_input\').val().length < 6 ){ renderError(error_text_password_short); validForm = false;}\n                else if (name && !(validateString(name,"username"))){ renderError(error_text_username_characters); validForm = false;}\n\n                   if (!validForm) {\n                    e.preventDefault();\n                    // reactivate the button if the form wasn\'t submitted\n                    $(\'#send\').removeAttr(\'disabled\');\n                    }\n                });\n        });\n    </script>\n\n    <div id="registrationForm" class="toolForm">\n        <form name="registration" id="registration" action="')
        __M_writer(unicode(form_action))
        __M_writer(u'" method="post" >\n            <div class="toolFormTitle">Create account</div>\n            <div class="form-row">\n                <label>Email address:</label>\n                <input id="email_input" type="text" name="email" value="')
        __M_writer(filters.html_escape(unicode(email )))
        __M_writer(u'" size="40"/>\n                <input type="hidden" name="redirect" value="')
        __M_writer(filters.html_escape(unicode(redirect )))
        __M_writer(u'" size="40"/>\n            </div>\n            <div class="form-row">\n                <label>Password:</label>\n                <input id="password_input" type="password" name="password" value="" size="40"/>\n            </div>\n            <div class="progress">\n                <div id="complexity-bar" class="progress-bar" role="progressbar">\n                    Strength\n                </div>\n            </div>\n            <div class="form-row">\n                <label>Confirm password:</label>\n                <input id="password_check_input" type="password" name="confirm" value="" size="40"/>\n            </div>\n            <div class="form-row">\n                <label>Public name:</label>\n                <input id="name_input" type="text" name="username" size="40" value="')
        __M_writer(filters.html_escape(unicode(username )))
        __M_writer(u'"/>\n')
        if t.webapp.name == 'galaxy':
            __M_writer(u'                    <div class="toolParamHelp" style="clear: both;">\n                        Your public name is an identifier that will be used to generate addresses for information\n                        you share publicly. Public names must be at least three characters in length and contain only\n                        lower-case letters, numbers, dots, underscores, and dashes (\'.\', \'_\', \'-\').\n                    </div>\n')
        else:
            __M_writer(u'                    <div class="toolParamHelp" style="clear: both;">\n                        Your public name provides a means of identifying you publicly within this tool shed. Public\n                        names must be at least three characters in length and contain only lower-case letters, numbers,\n                        dots, underscores, and dashes (\'.\', \'_\', \'-\'). You cannot change your public name after you have\n                        created a repository in this Tool Shed.\n                    </div>\n')
        __M_writer(u'            </div>\n')
        if trans.app.config.smtp_server and trans.app.config.mailing_join_addr:
            __M_writer(u'                <div class="form-row">\n                    <label>Subscribe to mailing list:</label>\n')
            if subscribe_checked:
                __M_writer(u'                        ')
                subscribe_check_box.checked = True 
                
                __M_writer(u'\n')
            __M_writer(u'                    ')
            __M_writer(unicode(subscribe_check_box.get_html()))
            __M_writer(u'\n                    <p>See <a href="http://galaxyproject.org/wiki/Mailing%20Lists" target="_blank">\n                    all Galaxy project mailing lists</a>.</p>\n                </div>\n')
        __M_writer(u'            <div id="for_bears">\n            If you see this, please leave following field blank.\n            <input type="text" name="bear_field" size="1" value=""/>\n            </div>\n            <div class="form-row">\n                <input type="submit" id="send" name="create_user_button" value="Submit"/>\n            </div>\n        </form>\n')
        if registration_warning_message:
            __M_writer(u'        <div class="alert alert-danger" style="margin: 30px 12px 12px 12px;">\n            ')
            __M_writer(unicode(registration_warning_message))
            __M_writer(u'\n        </div>\n')
        __M_writer(u'    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"128": 27, "179": 135, "134": 22, "142": 22, "143": 23, "16": 1, "174": 130, "150": 57, "202": 192, "201": 189, "175": 130, "185": 160, "32": 20, "176": 134, "165": 57, "38": 0, "177": 134, "45": 8, "46": 9, "47": 18, "48": 20, "49": 24, "50": 28, "51": 55, "52": 194, "181": 152, "182": 153, "183": 154, "184": 159, "180": 152, "58": 30, "187": 168, "188": 169, "189": 171, "190": 172, "191": 172, "193": 172, "194": 174, "195": 174, "196": 174, "197": 179, "198": 187, "199": 188, "72": 30, "73": 31, "74": 31, "75": 33, "76": 34, "77": 35, "78": 35, "79": 37, "80": 38, "81": 38, "82": 38, "83": 40, "84": 43, "85": 44, "86": 44, "87": 44, "88": 46, "89": 47, "90": 49, "91": 49, "92": 53, "186": 167, "144": 23, "98": 11, "166": 59, "178": 135, "105": 11, "106": 12, "208": 202, "173": 64, "113": 17, "119": 26, "200": 189, "126": 26, "127": 27}, "uri": "/user/register.mako", "filename": "templates/user/register.mako"}
__M_END_METADATA
"""
