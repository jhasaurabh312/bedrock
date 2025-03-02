# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.conf.urls import url

from .util import page
from . import views
from bedrock.redirects.util import redirect


urlpatterns = (
    url(r'^$', views.home_view, name='mozorg.home'),
    page('about', 'mozorg/about.html'),
    page('about/manifesto', 'mozorg/about/manifesto.html'),
    page('about/manifesto/details', 'mozorg/about/manifesto-details.html'),
    page('about/leadership', 'mozorg/about/leadership.html'),
    page('about/policy/lean-data', 'mozorg/about/policy/lean-data/index.html'),
    page('about/policy/lean-data/build-security', 'mozorg/about/policy/lean-data/build-security.html'),
    page('about/policy/lean-data/stay-lean', 'mozorg/about/policy/lean-data/stay-lean.html'),
    page('about/policy/lean-data/engage-users', 'mozorg/about/policy/lean-data/engage-users.html'),
    page('about/policy/patents', 'mozorg/about/policy/patents/index.html'),
    page('about/policy/patents/license', 'mozorg/about/policy/patents/license.html'),
    page('about/policy/patents/license/1.0', 'mozorg/about/policy/patents/license-1.0.html'),
    page('about/policy/patents/guide', 'mozorg/about/policy/patents/guide.html'),
    page('book', 'mozorg/book.html'),
    url('^credits/$', views.credits_view, name='mozorg.credits'),
    page('credits/faq', 'mozorg/credits-faq.html'),
    page('developer/browsertest', 'mozorg/browser-test.html'),
    page('about/partnerships/distribution', 'mozorg/partnerships-distribution.html'),
    page('about/history', 'mozorg/about/history.html'),
    # Bug 981063, catch all for old calendar urls.
    # must be here to avoid overriding the above
    redirect(r'^projects/calendar/', 'https://www.thunderbird.net/calendar/', locale_prefix=False),
    page('mission', 'mozorg/mission.html'),
    url('^about/forums/$', views.forums_view, name='mozorg.about.forums.forums'),
    page('about/forums/etiquette', 'mozorg/about/forums/etiquette.html'),
    page('about/forums/cancellation', 'mozorg/about/forums/cancellation.html'),
    page('about/governance', 'mozorg/about/governance/governance.html'),
    page('about/governance/roles', 'mozorg/about/governance/roles.html'),
    page('about/governance/policies', 'mozorg/about/governance/policies/policies.html'),
    page('about/governance/policies/commit', 'mozorg/about/governance/policies/commit.html'),
    page('about/governance/policies/commit/access-policy',
         'mozorg/about/governance/policies/commit/access-policy.html'),
    page('about/governance/policies/commit/requirements',
         'mozorg/about/governance/policies/commit/requirements.html'),
    page('about/governance/policies/security-group/bugs',
         'mozorg/about/governance/policies/security/bugs.html'),
    page('about/governance/policies/security-group/tld-idn',
         'mozorg/about/governance/policies/security/tld-idn.html'),
    page('about/governance/policies/security-group/membership',
         'mozorg/about/governance/policies/security/membership.html'),
    page('about/governance/policies/security-group/certs',
         'mozorg/about/governance/policies/security/certs/index.html'),
    page('about/governance/policies/security-group/certs/policy',
         'mozorg/about/governance/policies/security/certs/policy.html'),
    page('about/governance/policies/security/plugin-whitelist-policy',
         'mozorg/about/governance/policies/security/plugin-whitelist-policy.html'),
    page('about/governance/organizations', 'mozorg/about/governance/organizations.html'),
    page('about/governance/policies/participation',
         'mozorg/about/governance/policies/participation.html'),
    page('about/governance/policies/participation/reporting',
         'mozorg/about/governance/policies/reporting.html'),
    page('about/governance/policies/module-ownership',
         'mozorg/about/governance/policies/module-ownership.html'),
    page('about/governance/policies/regressions',
         'mozorg/about/governance/policies/regressions.html'),

    page('about/policy/transparency', 'mozorg/about/policy/transparency/index.html'),
    page('about/policy/transparency/jan-dec-2015',
         'mozorg/about/policy/transparency/jan-dec-2015.html'),
    page('about/policy/transparency/jan-jun-2016',
         'mozorg/about/policy/transparency/jan-jun-2016.html'),
    page('about/policy/transparency/jul-dec-2016',
         'mozorg/about/policy/transparency/jul-dec-2016.html'),
    page('about/policy/transparency/jan-jun-2017',
         'mozorg/about/policy/transparency/jan-jun-2017.html'),
    page('about/policy/transparency/jul-dec-2017',
         'mozorg/about/policy/transparency/jul-dec-2017.html'),
    page('about/policy/transparency/jan-jun-2018',
         'mozorg/about/policy/transparency/jan-jun-2018.html'),

    page('contact', 'mozorg/contact/contact-landing.html'),
    page('contact/spaces', 'mozorg/contact/spaces/spaces-landing.html'),
    page('contact/spaces/mountain-view', 'mozorg/contact/spaces/mountain-view.html'),
    page('contact/spaces/beijing', 'mozorg/contact/spaces/beijing.html'),
    page('contact/spaces/berlin', 'mozorg/contact/spaces/berlin.html'),
    page('contact/spaces/london', 'mozorg/contact/spaces/london.html'),
    page('contact/spaces/paris', 'mozorg/contact/spaces/paris.html'),
    page('contact/spaces/portland', 'mozorg/contact/spaces/portland.html'),
    page('contact/spaces/san-francisco', 'mozorg/contact/spaces/san-francisco.html'),
    page('contact/spaces/taipei', 'mozorg/contact/spaces/taipei.html'),
    page('contact/spaces/toronto', 'mozorg/contact/spaces/toronto.html'),
    page('contact/spaces/vancouver', 'mozorg/contact/spaces/vancouver.html'),

    page('contact/communities', 'mozorg/contact/communities/communities-landing.html'),
    page('contact/communities/north-america',
         'mozorg/contact/communities/north-america/landing.html'),
    page('contact/communities/latin-america',
         'mozorg/contact/communities/latin-america/landing.html'),
    page('contact/communities/europe', 'mozorg/contact/communities/europe/landing.html'),
    page('contact/communities/asia-south-pacific',
         'mozorg/contact/communities/asia-south-pacific/landing.html'),
    page('contact/communities/antarctica', 'mozorg/contact/communities/other/antarctica.html'),
    page('contact/communities/africa-middle-east',
         'mozorg/contact/communities/africa-middle-east/landing.html'),
    page('contact/communities/arabic', 'mozorg/contact/communities/other/arabic.html'),
    page('contact/communities/hispano', 'mozorg/contact/communities/other/hispano.html'),
    page('contact/communities/francophone', 'mozorg/contact/communities/other/francophone.html'),
    page('contact/communities/balkans', 'mozorg/contact/communities/other/balkans.html'),

    page('contact/communities/canada', 'mozorg/contact/communities/north-america/canada.html'),
    page('contact/communities/united-states',
         'mozorg/contact/communities/north-america/united-states.html'),
    page('contact/communities/argentina',
         'mozorg/contact/communities/latin-america/argentina.html'),
    page('contact/communities/bolivia',
         'mozorg/contact/communities/latin-america/bolivia.html'),
    page('contact/communities/brazil',
         'mozorg/contact/communities/latin-america/brazil.html'),
    page('contact/communities/chile',
         'mozorg/contact/communities/latin-america/chile.html'),
    page('contact/communities/colombia',
         'mozorg/contact/communities/latin-america/colombia.html'),
    page('contact/communities/costa-rica',
         'mozorg/contact/communities/latin-america/costa-rica.html'),
    page('contact/communities/cuba',
         'mozorg/contact/communities/latin-america/cuba.html'),
    page('contact/communities/ecuador',
         'mozorg/contact/communities/latin-america/ecuador.html'),
    page('contact/communities/mexico',
         'mozorg/contact/communities/latin-america/mexico.html'),
    page('contact/communities/nicaragua',
         'mozorg/contact/communities/latin-america/nicaragua.html'),
    page('contact/communities/paraguay',
         'mozorg/contact/communities/latin-america/paraguay.html'),
    page('contact/communities/peru',
         'mozorg/contact/communities/latin-america/peru.html'),
    page('contact/communities/uruguay',
         'mozorg/contact/communities/latin-america/uruguay.html'),
    page('contact/communities/venezuela',
         'mozorg/contact/communities/latin-america/venezuela.html'),

    page('contact/communities/albania', 'mozorg/contact/communities/europe/albania.html'),
    page('contact/communities/armenia', 'mozorg/contact/communities/europe/armenia.html'),
    page('contact/communities/austria', 'mozorg/contact/communities/europe/austria.html'),
    page('contact/communities/basque', 'mozorg/contact/communities/europe/basque.html'),
    page('contact/communities/belgium', 'mozorg/contact/communities/europe/belgium.html'),
    page('contact/communities/bosnia-and-herzegovina',
         'mozorg/contact/communities/europe/bosnia-and-herzegovina.html'),
    page('contact/communities/bulgaria', 'mozorg/contact/communities/europe/bulgaria.html'),
    page('contact/communities/catalan', 'mozorg/contact/communities/europe/catalan.html'),
    page('contact/communities/croatia', 'mozorg/contact/communities/europe/croatia.html'),
    page('contact/communities/czech-republic', 'mozorg/contact/communities/europe/czech-republic.html'),
    page('contact/communities/denmark', 'mozorg/contact/communities/europe/denmark.html'),
    page('contact/communities/estonia', 'mozorg/contact/communities/europe/estonia.html'),
    page('contact/communities/finland', 'mozorg/contact/communities/europe/finland.html'),
    page('contact/communities/france', 'mozorg/contact/communities/europe/france.html'),
    page('contact/communities/germany', 'mozorg/contact/communities/europe/germany.html'),
    page('contact/communities/greece', 'mozorg/contact/communities/europe/greece.html'),
    page('contact/communities/hungary', 'mozorg/contact/communities/europe/hungary.html'),
    page('contact/communities/ireland', 'mozorg/contact/communities/europe/ireland.html'),
    page('contact/communities/italy', 'mozorg/contact/communities/europe/italy.html'),
    page('contact/communities/kosovo', 'mozorg/contact/communities/europe/kosovo.html'),
    page('contact/communities/lithuania', 'mozorg/contact/communities/europe/lithuania.html'),
    page('contact/communities/norway', 'mozorg/contact/communities/europe/norway.html'),
    page('contact/communities/poland', 'mozorg/contact/communities/europe/poland.html'),
    page('contact/communities/portugal', 'mozorg/contact/communities/europe/portugal.html'),
    page('contact/communities/macedonia', 'mozorg/contact/communities/europe/macedonia.html'),
    page('contact/communities/montenegro', 'mozorg/contact/communities/europe/montenegro.html'),
    page('contact/communities/romania', 'mozorg/contact/communities/europe/romania.html'),
    page('contact/communities/russia', 'mozorg/contact/communities/europe/russia.html'),
    page('contact/communities/serbia', 'mozorg/contact/communities/europe/serbia.html'),
    page('contact/communities/slovakia', 'mozorg/contact/communities/europe/slovakia.html'),
    page('contact/communities/slovenia', 'mozorg/contact/communities/europe/slovenia.html'),
    page('contact/communities/spain', 'mozorg/contact/communities/europe/spain.html'),
    page('contact/communities/sweden', 'mozorg/contact/communities/europe/sweden.html'),
    page('contact/communities/switzerland', 'mozorg/contact/communities/europe/switzerland.html'),
    page('contact/communities/the-netherlands', 'mozorg/contact/communities/europe/the-netherlands.html'),
    page('contact/communities/turkey', 'mozorg/contact/communities/europe/turkey.html'),
    page('contact/communities/ukraine', 'mozorg/contact/communities/europe/ukraine.html'),
    page('contact/communities/united-kingdom', 'mozorg/contact/communities/europe/united-kingdom.html'),

    page('contact/communities/australia',
         'mozorg/contact/communities/asia-south-pacific/australia.html'),
    page('contact/communities/bangladesh',
         'mozorg/contact/communities/asia-south-pacific/bangladesh.html'),
    page('contact/communities/cambodia',
         'mozorg/contact/communities/asia-south-pacific/cambodia.html'),
    page('contact/communities/china',
         'mozorg/contact/communities/asia-south-pacific/china.html'),
    page('contact/communities/hong-kong',
         'mozorg/contact/communities/asia-south-pacific/hong-kong.html'),
    page('contact/communities/india',
         'mozorg/contact/communities/asia-south-pacific/india.html'),
    page('contact/communities/indonesia',
         'mozorg/contact/communities/asia-south-pacific/indonesia.html'),
    page('contact/communities/japan',
         'mozorg/contact/communities/asia-south-pacific/japan.html'),
    page('contact/communities/kerala',
         'mozorg/contact/communities/asia-south-pacific/kerala.html'),
    page('contact/communities/malaysia',
         'mozorg/contact/communities/asia-south-pacific/malaysia.html'),
    page('contact/communities/myanmar',
         'mozorg/contact/communities/asia-south-pacific/myanmar.html'),
    page('contact/communities/nepal',
         'mozorg/contact/communities/asia-south-pacific/nepal.html'),
    page('contact/communities/pakistan',
         'mozorg/contact/communities/asia-south-pacific/pakistan.html'),
    page('contact/communities/philippines',
         'mozorg/contact/communities/asia-south-pacific/philippines.html'),
    page('contact/communities/singapore',
         'mozorg/contact/communities/asia-south-pacific/singapore.html'),
    page('contact/communities/south-korea',
         'mozorg/contact/communities/asia-south-pacific/south-korea.html'),
    page('contact/communities/sri-lanka',
         'mozorg/contact/communities/asia-south-pacific/sri-lanka.html'),
    page('contact/communities/taiwan',
         'mozorg/contact/communities/asia-south-pacific/taiwan.html'),
    page('contact/communities/thailand',
         'mozorg/contact/communities/asia-south-pacific/thailand.html'),
    page('contact/communities/vietnam',
         'mozorg/contact/communities/asia-south-pacific/vietnam.html'),

    page('contact/communities/algeria',
         'mozorg/contact/communities/africa-middle-east/algeria.html'),
    page('contact/communities/cameroon',
         'mozorg/contact/communities/africa-middle-east/cameroon.html'),
    page('contact/communities/ivory-coast',
         'mozorg/contact/communities/africa-middle-east/ivory-coast.html'),
    page('contact/communities/egypt',
         'mozorg/contact/communities/africa-middle-east/egypt.html'),
    page('contact/communities/ghana',
         'mozorg/contact/communities/africa-middle-east/ghana.html'),
    page('contact/communities/israel',
         'mozorg/contact/communities/africa-middle-east/israel.html'),
    page('contact/communities/jordan',
         'mozorg/contact/communities/africa-middle-east/jordan.html'),
    page('contact/communities/kenya',
         'mozorg/contact/communities/africa-middle-east/kenya.html'),
    page('contact/communities/mauritius',
         'mozorg/contact/communities/africa-middle-east/mauritius.html'),
    page('contact/communities/palestine',
         'mozorg/contact/communities/africa-middle-east/palestine.html'),
    page('contact/communities/senegal',
         'mozorg/contact/communities/africa-middle-east/senegal.html'),
    page('contact/communities/tunisia',
         'mozorg/contact/communities/africa-middle-east/tunisia.html'),
    page('contact/communities/uganda',
         'mozorg/contact/communities/africa-middle-east/uganda.html'),
    page('contact/communities/zimbabwe',
         'mozorg/contact/communities/africa-middle-east/zimbabwe.html'),

    page('MPL', 'mozorg/mpl/index.html'),
    page('MPL/historical', 'mozorg/mpl/historical.html'),
    page('MPL/license-policy', 'mozorg/mpl/license-policy.html'),
    page('MPL/headers', 'mozorg/mpl/headers/index.html'),
    page('MPL/1.1', 'mozorg/mpl/1.1/index.html'),
    page('MPL/1.1/FAQ', 'mozorg/mpl/1.1/faq.html'),
    page('MPL/1.1/annotated', 'mozorg/mpl/1.1/annotated/index.html'),
    page('MPL/2.0', 'mozorg/mpl/2.0/index.html'),
    page('MPL/2.0/FAQ', 'mozorg/mpl/2.0/faq.html'),
    page('MPL/2.0/Revision-FAQ', 'mozorg/mpl/2.0/revision-faq.html'),
    page('MPL/2.0/combining-mpl-and-gpl', 'mozorg/mpl/2.0/combining-mpl-and-gpl.html'),
    page('MPL/2.0/differences', 'mozorg/mpl/2.0/differences.html'),
    page('MPL/2.0/permissive-code-into-mpl', 'mozorg/mpl/2.0/permissive-code-into-mpl.html'),

    page('contribute', 'mozorg/contribute/index.html'),
    url('^contribute/embed/$', views.contribute_embed,
        name='mozorg.contribute_embed'),
    page('contribute/events', 'mozorg/contribute/events.html'),
    page('contribute/stories', 'mozorg/contribute/stories.html'),
    page('contribute/stories/faye', 'mozorg/contribute/story-faye.html'),
    page('contribute/stories/michael', 'mozorg/contribute/story-michael.html'),
    page('contribute/stories/ruben', 'mozorg/contribute/story-ruben.html'),
    page('contribute/stories/shreyas', 'mozorg/contribute/story-shreyas.html'),
    url(r'^contributor-data/(?P<source_name>[a-z]{2,20})\.json$', views.mozid_data_view,
        name='mozorg.contributor-data'),
    url('^internet-health/$', views.IHView.as_view(), name='mozorg.internet-health'),
    page('internet-health/privacy-security', 'mozorg/internet-health/privacy-security.html'),
    page('internet-health/digital-inclusion', 'mozorg/internet-health/digital-inclusion.html'),
    page('internet-health/open-innovation', 'mozorg/internet-health/open-innovation.html'),
    page('internet-health/web-literacy', 'mozorg/internet-health/web-literacy.html'),
    page('internet-health/decentralization', 'mozorg/internet-health/decentralization.html'),

    url(r'^moss/$', views.moss_view, name='mozorg.moss.index'),
    page('moss/foundational-technology', 'mozorg/moss/foundational-technology.html'),
    page('moss/mission-partners', 'mozorg/moss/mission-partners.html'),
    page('moss/mission-partners-india', 'mozorg/moss/mission-partners-india.html'),
    page('moss/secure-open-source', 'mozorg/moss/secure-open-source.html'),

    url(r'^oauth/fxa/$', views.oauth_fxa, name='mozorg.oauth.fxa'),
    url(r'^oauth/fxa/error/$', views.oauth_fxa_error, name='mozorg.oauth.fxa-error'),

    page('plugincheck', 'mozorg/plugincheck.html'),
    url(r'^robots\.txt$', views.Robots.as_view(), name='robots.txt'),
    url('^technology/$', views.TechnologyView.as_view(), name='mozorg.technology'),
    page('technology/what-is-a-browser', 'mozorg/what-is-a-browser.html'),
    page('technology/update-your-browser', 'mozorg/update-browser.html'),
    page('technology/incognito-browser', 'mozorg/incognito-browser.html'),
    page('technology/browser-history', 'mozorg/browser-history.html'),

    url('^developer/$', views.DeveloperView.as_view(), name='mozorg.developer'),
    page('developer/css-grid', 'mozorg/developer/css-grid-demo.html'),

    # namespaces
    url(r'^2004/em-rdf$', views.namespaces, {'namespace': 'em-rdf'}),
    url(r'^2005/app-update$', views.namespaces, {'namespace': 'update'}),
    url(r'^2006/addons-blocklist$', views.namespaces, {'namespace': 'addons-bl'}),
    url(r'^2006/browser/search/$', views.namespaces, {'namespace': 'mozsearch'}),
    url(r'^keymaster/gatekeeper/there\.is\.only\.xul$', views.namespaces, {'namespace': 'xul'}),
    url(r'^microsummaries/0\.1$', views.namespaces, {'namespace': 'microsummaries'}),
    url(r'^projects/xforms/2005/type$', views.namespaces, {'namespace': 'xforms-type'}),
    url(r'^xbl$', views.namespaces, {'namespace': 'xbl'}),

    page('locales', 'mozorg/locales.html'),
)
