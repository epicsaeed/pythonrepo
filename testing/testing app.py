    elif request.method == 'POST':
        #updates details of passed product id
        payload = request.get_json()

        #checks if payload is empty, returns 400 if so
        if not payload:
            return jsonify(),400
            
        #returns a 400 if no known parameters are given
        name = payload.get('name')
        size = payload.get('size')
        color = payload.get('color')
        in_stock = payload.get('in_stock')


        #manipulates passed parameteres for updating 
        if "name" in payload:
            print("name in payload")#         testing
            name = payload['name'] 
            if not name:
                print("but name is empty so it will be null")#         testing
                name = "N/A"
            query = "UPDATE data SET name =? WHERE productid=?"
            cur.execute(query,(name,id))
            conn.commit()
            print("commited name")

        if "size" in payload:
            size = payload['size']
            if not size:
                size = "N/A"
            query = "UPDATE data SET size =? WHERE productid=?"
            cur.execute(query,(size,id))
            conn.commit()

        if "color" in payload:
            color = payload['color']
            if not color:
                color = "N/A"
            query = "UPDATE data SET color =? WHERE productid=?"
            cur.execute(query,(color,id))
            conn.commit()

        if "in_stock" in payload:
            instock = str(payload['in_stock'])
            if not instock.isdigit() or not instock:
                print("instock is invalid")
                return jsonify(),404
            query = "UPDATE data SET instock =? WHERE productid=?"
            cur.execute(query,(payload['in_stock'],id))
            conn.commit()
        return jsonify(),200