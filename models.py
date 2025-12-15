class UnderWriter:
    def __init__(self, uid, name, dob, joining_date, password):
        self.uid = uid
        self.name = name
        self.dob = dob
        self.joining_date = joining_date
        self.password = password

    def to_dict(self):
        return {
            "uid": self.uid,
            "name": self.name,
            "dob": self.dob,
            "joining_date": self.joining_date,
            "password": self.password
        }

    @staticmethod
    def from_dict(data):
        return UnderWriter(
            data["uid"],
            data["name"],
            data["dob"],
            data["joining_date"],
            data["password"]
        )

class VehiclePolicy:
    def __init__(self, policy_no, vehicle_no, vehicle_type, customer_name, engine_no, chasis_no, phone_no, policy_type, premium_amt, from_date, to_date, underwriter_id):
        self.policy_no = policy_no
        self.vehicle_no = vehicle_no
        self.vehicle_type = vehicle_type
        self.customer_name = customer_name
        self.engine_no = engine_no
        self.chasis_no = chasis_no
        self.phone_no = phone_no
        self.policy_type = policy_type
        self.premium_amt = premium_amt
        self.from_date = from_date
        self.to_date = to_date
        self.underwriter_id = underwriter_id

    def to_dict(self):
        return {
            "policy_no": self.policy_no,
            "vehicle_no": self.vehicle_no,
            "vehicle_type": self.vehicle_type,
            "customer_name": self.customer_name,
            "engine_no": self.engine_no,
            "chasis_no": self.chasis_no,
            "phone_no": self.phone_no,
            "policy_type": self.policy_type,
            "premium_amt": self.premium_amt,
            "from_date": self.from_date,
            "to_date": self.to_date,
            "underwriter_id": self.underwriter_id
        }

    @staticmethod
    def from_dict(data):
        return VehiclePolicy(
            data["policy_no"],
            data["vehicle_no"],
            data["vehicle_type"],
            data["customer_name"],
            data["engine_no"],
            data["chasis_no"],
            data["phone_no"],
            data["policy_type"],
            data["premium_amt"],
            data["from_date"],
            data["to_date"],
            data["underwriter_id"]
        )
