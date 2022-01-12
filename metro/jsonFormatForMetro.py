import json, os, glob
path_to_json = 'ann/'
os.mkdir(os.path.join("formattedJsons"))
output="formattedJsons/"

for file_name in sorted([file for file in os.listdir(path_to_json) if file.endswith('.json')]):
	with open(path_to_json + file_name) as json_file:
		base=[{
		        "dataset_name": "",
		        "image_link": "",
		        "annotation_type": "image",
		        
				        "annotation_objects":
				        [
				        {
				            "vehicle":
				            {
				            "presence":0,
				            "bbox":[
				            ]

				            }
				                
				            ,
				            "license_plate":{
				            "presence": 0,
				            "bbox":[
				            ]
				            }
				            
				        }
				        ],
				        "annotation_attributes":
				        [
				        {
				            "vehicle":
				            {
				               "Type": None,
				                "Pose": None,
				                "Model": None,
				                "Make": None,
				                "Color": None
				            },
				            "license_plate":
				            {
				            	"Difficulty Score": None,
				                "Value": None,
				                "Occlusion": None
				            }
				            
				        }
				        ]
			       
		    }]
		


		base[0]["dataset_name"]=str(file_name)

		data = json.load(json_file)
		objectt=0
		classs=[]
		for obj in data["objects"]:
			vp=0
			pp=0
			if data["objects"][objectt]["classTitle"]=="Vehicle":
				classs.append(data["objects"][objectt]["classTitle"])
				a=data["objects"][objectt]["points"]["exterior"][0][0]
				b=data["objects"][objectt]["points"]["exterior"][0][1]
				c=data["objects"][objectt]["points"]["exterior"][1][0]
				d=data["objects"][objectt]["points"]["exterior"][1][1]

				base[0]["annotation_objects"][0]["vehicle"]["bbox"].append(a)
				base[0]["annotation_objects"][0]["vehicle"]["bbox"].append(b)
				base[0]["annotation_objects"][0]["vehicle"]["bbox"].append(c)
				base[0]["annotation_objects"][0]["vehicle"]["bbox"].append(d)
				base[0]["annotation_objects"][0]["vehicle"]["presence"]=1
				vp=1
			elif data["objects"][objectt]["classTitle"]=="License Plate":
				classs.append(data["objects"][objectt]["classTitle"])
				a=data["objects"][objectt]["points"]["exterior"][0][0]
				b=data["objects"][objectt]["points"]["exterior"][0][1]
				c=data["objects"][objectt]["points"]["exterior"][1][0]
				d=data["objects"][objectt]["points"]["exterior"][1][1]





				base[0]["annotation_objects"][0]["license_plate"]["bbox"].append(a)
				base[0]["annotation_objects"][0]["license_plate"]["bbox"].append(b)
				base[0]["annotation_objects"][0]["license_plate"]["bbox"].append(c)
				base[0]["annotation_objects"][0]["license_plate"]["bbox"].append(d)
				base[0]["annotation_objects"][0]["license_plate"]["presence"]=1
				pp=1

			Type=""
			Pose=""
			Model=""
			Make=""
			Color=""
			DifficultyScore=""
			Value=""
			occ=0
			tag=0

			for tags in data["objects"][objectt]["tags"]:
				if data["objects"][objectt]["tags"][tag]["name"]=="Type":
					Type=data["objects"][objectt]["tags"][tag]["value"]
				if data["objects"][objectt]["tags"][tag]["name"]=="Pose":
					Pose=data["objects"][objectt]["tags"][tag]["value"]
				if data["objects"][objectt]["tags"][tag]["name"]=="Model":
					Model=data["objects"][objectt]["tags"][tag]["value"]
				if data["objects"][objectt]["tags"][tag]["name"]=="Make":
					Make=data["objects"][objectt]["tags"][tag]["value"]
				if data["objects"][objectt]["tags"][tag]["name"]=="Color":
					Color=data["objects"][objectt]["tags"][tag]["value"]
				if data["objects"][objectt]["tags"][tag]["name"]=="Difficulty Score":
					DifficultyScore=int(data["objects"][objectt]["tags"][tag]["value"])
				if data["objects"][objectt]["tags"][tag]["name"]=="Value":
					Value=data["objects"][objectt]["tags"][tag]["value"]
				if data["objects"][objectt]["tags"][tag]["name"]=="Occlusion_1":
					occ=1

				tag+=1
			if data["objects"][objectt]["classTitle"]=="Vehicle":
				
				base[0]["annotation_attributes"][0]["vehicle"]["Type"]=Type
				base[0]["annotation_attributes"][0]["vehicle"]["Pose"]=Pose
				base[0]["annotation_attributes"][0]["vehicle"]["Model"]=Model
				base[0]["annotation_attributes"][0]["vehicle"]["Make"]=Make
				base[0]["annotation_attributes"][0]["vehicle"]["Color"]=Color
				
			elif data["objects"][objectt]["classTitle"]=="License Plate":
				
				if DifficultyScore!="":
					base[0]["annotation_attributes"][0]["license_plate"]["Difficulty Score"]=DifficultyScore
				else:
					base[0]["annotation_attributes"][0]["license_plate"]["Difficulty Score"]=None
				if Value !="":
					base[0]["annotation_attributes"][0]["license_plate"]["Value"]=Value
				else:
					base[0]["annotation_attributes"][0]["license_plate"]["Value"]=None
				if occ!=0:
					base[0]["annotation_attributes"][0]["license_plate"]["Occlusion"]=1
				else:
					base[0]["annotation_attributes"][0]["license_plate"]["Occlusion"]=0
			


			objectt+=1	


	
		



		jsonFile = open(output+ file_name, "w+")
		jsonFile.write(json.dumps(base, indent=4))
		jsonFile.close()

		#json_formatted_str = json.dumps(obj, indent=4)
		

	









				
				
				





			





				
				

			

			
			
