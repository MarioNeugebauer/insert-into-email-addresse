# input_file
# output_file
# keep_original_address_in_list
# make_csl make only one line with comma separated emails
def generate_emails(input_file, output_file, keep_original_address_in_list, make_csl):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        total_lines = sum(1 for _ in infile)
        infile.seek(0)  # Zurücksetzen des Dateizeigers auf den Anfang der Datei
        for index, line in enumerate(infile, start=1):
        # for line in infile:
            email = line.strip()
            if '@' in email:
                username, domain = email.split('@')
                new_email1 = f"{username}.e1@{domain}"
                new_email2 = f"{username}.e2@{domain}"
                if make_csl:
                    if keep_original_address_in_list:
                        outfile.write(f"{email}, ")
                    outfile.write(f"{new_email1}, ")
                    outfile.write(f"{new_email2}")
                    if index < total_lines:
                        outfile.write(f", ")

                else:
                    if keep_original_address_in_list:
                        outfile.write(f"{email}\n")
                    outfile.write(f"{new_email1}\n")
                    outfile.write(f"{new_email2}\n")

# Example
input_filename = '/mnt/c/daten/temp/schule/input_emails.txt'  # File with email addresses as input
output_filename = '/mnt/c/daten/temp/schule/output_emails.txt'  # File to write the email addresses

generate_emails(input_filename, output_filename, False, True)
