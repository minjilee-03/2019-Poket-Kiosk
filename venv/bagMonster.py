import mysql.connector
cnx = mysql.connector.connect(user="root", password="mirim", host="127.0.0.1", port=3306, database="poketkiosk")
cursor = cnx.cursor()

selectMonster = ""
class bagmonster:
    #가방에 넣는 메서드
    def intoBag(self):
        m_mon = user.mypocketmon.split(",")
        usermon = user.pocketmon.split(",")
        for i in range(0, len(m_mon) - 1):
            if m_mon[i] != "":
                usermon += m_mon[i] + ","
        sql = "UPDATE user SET pocketmon = '" + usermon +"' WHERE id=" + str(user.id)
        cursor.execute(sql)
        cnx.commit()

    def outBag(self, b_pocketmon):
        m_pocketmon = user.mypocketmon.split(",")
        self.b_pocketmon = user.pocketmon - m_pocketmon

        for i in range(0, len(b_pocketmon) - 1):
            if b_pocketmon[i] != m_pocketmon:
                m_pocketmon = b_pocketmon
                sql = "update user set mypocketmon = '" + self.m_pocketmon + "',where id = " + str(user.id)
                cursor.execute(sql)
                cnx.commit()








