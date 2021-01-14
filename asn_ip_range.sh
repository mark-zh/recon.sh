whois -h whois.radb.net  -- '-i origin $1' | grep -Eo "([0-9.]+){4}/[0-9]+" | uniq
