import os
import datetime

def generate_sitemap(domain, urls,changefreq, priority,save_path):
    # 创建Sitemap头部
    sitemap_header = '<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n'
    sitemap_header += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'

    # 创建Sitemap主体
    sitemap_body = ''
    for url in urls:
        sitemap_body += '    <url>\n'
        sitemap_body += f'        <loc>{domain}{url}</loc>\n'
        sitemap_body += f'        <lastmod>{datetime.date.today().isoformat()}</lastmod>\n'
        sitemap_body += f'        <changefreq>{changefreq}</changefreq>\n'
        sitemap_body += f'        <priority>{priority}</priority>\n'
        sitemap_body += '    </url>\n'

    # 创建Sitemap尾部
    sitemap_footer = '</urlset>'

    # 将头部、主体和尾部组合成Sitemap
    sitemap = sitemap_header + sitemap_body + sitemap_footer

    # 将Sitemap保存到文件
    with open(os.path.join(save_path, 'sitemap.xml'), 'w') as f:
        f.write(sitemap)

# 示例使用
if __name__ == '__main__':
    domain = 'https://mzfqy.site'
    urls = ['/', '/ai/', '/code/', '/his/', '/life/', '/money/', '/shop/','/about.html']
    # always, hourly, daily, weekly, monthly, yearly, never
    # default:weekly
    changefreq = 'daily'
    # 0.5-1.0 之间
    priority = '0.6'
    save_path = '.'
    generate_sitemap(domain, urls,changefreq,priority, save_path)