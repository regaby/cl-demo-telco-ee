# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2021  Leonardo Bozzi  (http://www.vangrow.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------------
{
    'name': 'demo-telco',
    'version': '12.0.0.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customización Telecomunicaciones',
    'author': 'Leonardo Bozzi',
    'depends': [
        # Applicaciones del Cliente
        'sale_management',
        'sale_subscription',
        'purchase',
        'stock',
        'hr',
        'note',
        'board',
        'calendar',
        'website',
        'helpdesk',
        'project',

        # Contabilidad
        'account',
        'account_accountant',
        'account_check',

        # Localización
        'l10n_ar',

        # Miscellaneous
        'base_address_city',
        'base_address_extended',

        # Utils
        'web_search_with_and',
        'auto_backup',
        'mass_editing',
        'server_global_parameters',
        'base_external_dbsource',
        'mail_activity_board',

        # Vangrow
        'bit_partner_neighborhood',
        'bit_account_journal_day_book_report',
        'bit_dashboard_iframe',
        'bit_late_payment_penalty',
        'bit_sale_order_template_ux',
        'bit_sale_order_type_ux',
        'bit_subscription_sale_order_proportional',
        'bit_subscription_seal',
        'bit_subscription_ticket',
        'bit_subscription_ux',

        'bit_ndm',
        'bit_ndm_ftth',
        'bit_ndm_ftth_zxr10',
        'bit_ndm_dhcp',
        'bit_ndm_network',
        'bit_ndm_snmp',
        'bit_ndm_ssh',
        'bit_ndm_telnet',
        'bit_subscription_ndm',

    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'env-ver': '2',
    'odoo-license': 'EE',
    'port': '8069',
    # 'server_user': ''

    'config': [
        # 'addons_path' is always computed looking for the repositories in sources
        # 'data_dir' is a fixed location inside docker odoo image

        # You should use 2 worker threads + 1 cron thread per available CPU,
        # and 1 CPU per 10 concurent users.
        # if ommited oe will calculate workers and cron´s based on # of cpu
            'workers = 4',
            'max_cron_threads = 1',

        # Number of requests a worker will process before being recycled and
        # restarted. Defaults to 8192 if ommited
            'limit_request = 8192',

        # Maximum allowed virtual memory per worker. If the limit is exceeded,
        # the worker is killed and recycled at the end of the current request.
        # Defaults to 640MB
            'limit_memory_soft = 2147483648',

        # Hard limit on virtual memory, any worker exceeding the limit will be
        # immediately killed without waiting for the end of the current request
        # processing. Defaults to 768MB.
            'limit_memory_hard = 2684354560',
        # Prevents the worker from using more than CPU seconds for each request.
        # If the limit is exceeded, the worker is killed. Defaults to 60 sec.
            'limit_time_cpu = 1200',

        # Prevents the worker from taking longer than seconds to process a request.
        # If the limit is exceeded, the worker is killed. Defaults to 120. Differs
        # from --limit-time-cpu in that this is a "wall time" limit including e.g.
        # SQL queries.
            'limit_time_real = 2400',

        # default CSV separator for import and export
            'csv_internal_sep = ,',

        # disable loading demo data for modules to be installed
            'without_demo = False',

        # Comma-separated list of server-wide modules, there are modules loaded
        # automatically even if you do not create any database.
            'server_wide_modules = base,web,dbfilter_from_header',

        # Filter listed database REGEXP
            'dbfilter =',

            'db_maxconn = 64',
            'db_name = False',
            'db_password = odoo',
            'db_port = 5432',
            'db_sslmode = prefer',
            'db_template = template0',
            'db_user = odoo',
            'demo = {}',
            'email_from = False',
            'geoip_database = /usr/share/GeoIP/GeoLite2-City.mmdb',
            'http_enable = True',
            'http_interface =',
            'http_port = 8069',
            'limit_time_real_cron = -1',
            'list_db = True',
            'log_db = False',
            'log_db_level = warning',
            'log_handler = :INFO',
            'log_level = info',
            'logfile = /var/log/odoo/odoo.log',
            'osv_memory_age_limit = 1.0',
            'osv_memory_count_limit = False',
            'pg_path =',

            'proxy_mode = True',
            'reportgz = False',
            'screencasts =',
            'screenshots = /tmp/odoo_tests',
            'smtp_password = False',
            'smtp_port = 25',
            'smtp_server = localhost',
            'smtp_ssl = False',
            'smtp_user = False',
            'syslog = False',
            'test_enable = False',
            'test_file =',
            'test_tags = None',
            "translate_modules = ['all']",
            'unaccent = False',
            'upgrade_path =',
    ],

    'git-repos': [
        'https://github.com/leobozzi/cl-demo-telco-ee.git',
        'https://github.com/leobozzi/odoo-addons-utils.git',
        'https://github.com/vangrow/odoo-modules.git -b 12.0',
        'https://github.com/vangrow/ndm.git -b 12.0',
        'https://github.com/leobozzi/enterprise.git -b 12.0',

        # Odoomates
        # ==========================================================================================
        # 'https://github.com/odoomates/odooapps odoomates-odooapps',

        # Gabriela Rivero
        # ==========================================================================================
        # 'https://github.com/regaby/odoo-custom regaby-odoo-custom',

        # OCA
        # ==========================================================================================
        # 'https://github.com/OCA/account-closing oca-account-closing',
        'https://github.com/OCA/account-financial-reporting oca-account-financial-reporting',  # noqa
        'https://github.com/OCA/account-financial-tools oca-account-financial-tools',
        'https://github.com/OCA/account-invoicing oca-account-invoicing',
        'https://github.com/OCA/account-payment oca-account-payment',
        # 'https://github.com/OCA/apps-store oca-apps-store',
        # 'https://github.com/OCA/bank-payment oca-bank-payment',
        'https://github.com/OCA/brand oca-brand',
        # 'https://github.com/OCA/business-requirement oca-business-requirement',
        'https://github.com/OCA/commission oca-commission',
        # 'https://github.com/OCA/contract oca-contract',
        # 'https://github.com/OCA/credit-control oca-credit-control',
        # 'https://github.com/OCA/crm oca-crm',
        # 'https://github.com/OCA/currency oca-currency',
        # 'https://github.com/OCA/ddmrp oca-ddmrp',
        # 'https://github.com/OCA/delivery-carrier oca-delivery-carrier',
        # 'https://github.com/OCA/e-commerce oca-e-commerce',
        # 'https://github.com/OCA/event oca-event',
        # 'https://github.com/OCA/field-service oca-field-service',
        'https://github.com/OCA/geospatial oca-geospatial',
        # 'https://github.com/OCA/helpdesk oca-helpdesk',
        # 'https://github.com/OCA/hr oca-hr',
        # 'https://github.com/OCA/hr-timesheet oca-hr-timesheet',
        # 'https://github.com/OCA/knowledge oca-knowledge',
        # 'https://github.com/OCA/management-system oca-management-system',
        # 'https://github.com/OCA/manufacture oca-manufacture',
        # 'https://github.com/OCA/manufacture-reporting oca-manufacture-reporting',
        # 'https://github.com/OCA/margin-analysis oca-margin-analysis',
        # 'https://github.com/OCA/multi-company oca-multi-company',
        # 'https://github.com/OCA/oca-custom oca-oca-custom',
        # 'https://github.com/OCA/operating-unit oca-operating-unit',
        'https://github.com/OCA/partner-contact oca-partner-contact',
        # 'https://github.com/OCA/pos oca-pos',
        'https://github.com/OCA/product-attribute oca-product-attribute',
        'https://github.com/OCA/product-pack oca-product-pack',
        'https://github.com/OCA/project oca-project',
        'https://github.com/OCA/project-reporting oca-project-reporting',
        # 'https://github.com/OCA/purchase-workflow oca-purchase-workflow',
        # 'https://github.com/OCA/queue oca-queue',
        # 'https://github.com/OCA/report-print-send oca-report-print-send',
        'https://github.com/OCA/reporting-engine oca-reporting-engine',
        # 'https://github.com/OCA/sale-reporting oca-sale-reporting',
        'https://github.com/OCA/sale-workflow oca-sale-workflow',
        # 'https://github.com/OCA/server-auth oca-server-auth',
        'https://github.com/OCA/server-backend oca-server-backend',
        'https://github.com/OCA/server-tools oca-server-tools',
        'https://github.com/OCA/server-ux oca-server-ux',
        'https://github.com/OCA/social oca-social',
        'https://github.com/OCA/stock-logistics-barcode oca-stock-logistics-barcode',
        'https://github.com/OCA/stock-logistics-reporting oca-stock-logistics-reporting',  # noqa
        'https://github.com/OCA/stock-logistics-transport oca-stock-logistics-transport',  # noqa
        'https://github.com/OCA/stock-logistics-warehouse oca-stock-logistics-warehouse',  # noqa
        'https://github.com/OCA/stock-logistics-workflow oca-stock-logistics-workflow',
        'https://github.com/OCA/timesheet oca-timesheet',
        # 'https://github.com/OCA/vertical-association oca-vertical-association',
        'https://github.com/OCA/web oca-web',
        'https://github.com/OCA/website oca-website',
        # 'https://github.com/OCA/bank-payment oca-bank-payment',
        'https://github.com/OCA/account-analytic oca-account-analytic',

        # ADHOC
        # ==========================================================================================
        'https://github.com/ingadhoc/account-analytic ingadhoc-account-analytic',
        'https://github.com/ingadhoc/account-invoicing ingadhoc-account-invoicing',
        'https://github.com/ingadhoc/odoo-argentina-ee ingadhoc-odoo-argentina-ee',
        'https://github.com/ingadhoc/account-financial-tools ingadhoc-account-financial-tools',  # noqa
        'https://github.com/ingadhoc/account-payment ingadhoc-account-payment',
        'https://github.com/ingadhoc/aeroo_reports ingadhoc-aeroo_reports',
        'https://github.com/ingadhoc/argentina-reporting ingadhoc-argentina-reporting',
        'https://github.com/ingadhoc/argentina-sale ingadhoc-argentina-sale',
        # 'https://github.com/ingadhoc/hr ingadhoc-hr',
        'https://github.com/ingadhoc/miscellaneous ingadhoc-miscellaneous',
        'https://github.com/ingadhoc/multi-company ingadhoc-multi-company',
        # 'https://github.com/ingadhoc/multi-store ingadhoc-multi-store',

        # Fix porque falla la instalacion de l10n_ar_ux
        'https://github.com/ingadhoc/odoo-argentina ingadhoc-odoo-argentina',

        # 'https://github.com/ingadhoc/partner ingadhoc-partner',
        'https://github.com/ingadhoc/product ingadhoc-product',
        'https://github.com/ingadhoc/project ingadhoc-project',
        'https://github.com/ingadhoc/purchase ingadhoc-purchase',
        'https://github.com/ingadhoc/reporting-engine ingadhoc-reporting-engine',
        'https://github.com/ingadhoc/sale ingadhoc-sale',
        'https://github.com/ingadhoc/odoo-support ingadhoc-odoo-support',
        'https://github.com/ingadhoc/stock ingadhoc-stock',
        'https://github.com/ingadhoc/website ingadhoc-website',
    ],
    'docker-images': [
       # 'odoo jobiols/odoo-jeo:12.0',
       # 'odoo lbozzi/odoo-docker-lb:12.0',
       'odoo lbozzi/odoo-docker-lb:12.0',
       'postgres postgres:11.1-alpine',
       'aeroo adhoc/aeroo-docs',
       'nginx nginx',
    ]
}
