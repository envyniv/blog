;; init.el --- appends this blog to the org publishing list
;;; Commentary:
;; The "get-project-directory" variable is from https://taingram.org/blog/org-mode-blog.html

;;; Code:

(defvar get-project-directory
  (file-name-directory (or load-file-name (buffer-file-name))))

(setq org-publish-project-alist
      '(("blog"
	 :base-directory get-project-directory
	 :publishing-directory "~/blog_out/"
	 :base-extension "org"
	 :exclude "index.org"
	 :html-head "<link rel='icon' type='image/svg+xml' href='https://envyniv.github.io/favicon.svg' /><link rel='stylesheet' type='text/css' href='https://envyniv.github.io/style.css' /><link rel='icon' type='image/png' href='https://envyniv.github.io/favicon.png' />"
	 :html-head-extra "<link rel='stylesheet' type='text/css' href='https://fonts.googleapis.com/css?family=Spinnaker'>"
	 :with-author nil
	 :with-email nil
	 :with-tasks nil
	 :with-timestamps nil
	 :with-toc t
	 :html-preamble "<embed type=\"text/html\" src=\"https://envyniv.github.io/header.html\" width=\"100%%\" height=\"250px\" />" ;took me 3 hours to figure out I needed to escape the %
	 :sitemap-title "Posts"
	 :sitemap-filename "index.org"
	 :auto-sitemap t
	 :sitemap-sort-files anti-chronologically
	 :sitemap-file-entry-format "%d - %t"
	 )))
