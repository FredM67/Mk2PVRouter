mkdir -p content/pdf
find content/drawio -name *.drawio -exec drawio --export --format pdf --output content/pdf/ {} \;