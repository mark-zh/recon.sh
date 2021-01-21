whois -h whois.radb.net  -- '-i origin ASnum' | grep -Eo "([0-9.]+){4}/[0-9]+" | uniq
