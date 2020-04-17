import json
import queries as q
import functions as f

      
#Query the developer details...
developer_details = f.run_query(q.developer_query)

#print out the developer details for verificatoin purpose on...
# json_formatted_str = json.dumps(own_projects, indent=2)
# print(\"developers projects: {}\".format(json_formatted_str))

#process the developer's project details

#for each project detect the language and framework used
#get each framework project's package dependency file and 
#process the content to detect the libraries used...
