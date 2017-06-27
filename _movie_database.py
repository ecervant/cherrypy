
class _movie_database:

    def __init__(self):
        self.movie_names = dict() # movie ID as key
        self.movie_genres = dict()
        self.users = dict() # user ID as key
        self.ratings = dict() # movie ID as key
        self.imgs = dict() #mid as key

    def load_movies(self, movie_file):
        mfile = open(movie_file, encoding = "ISO-8859-1")
        for movie in mfile:
            movie = movie.strip("\n")
            m = movie.split("::")
            mid = int(m[0])
            name = m[1]
            genre = m[2]
            self.movie_names[mid] = name
            self.movie_genres[mid] = genre
        mfile.close()

    def load_movie(self, movie_file, mid):
        mfile = open(movie_file, encoding = "ISO-8859-1")
        for movie in mfile:
            movie = movie.strip("\n")
            m = movie.split("::")
            idd = int(m[0])
            if mid == idd:
                name = m[1]
                genre = m[2]
                self.movie_names[mid] = name
                self.movie_genres[mid] = genre
        mfile.close()


    def get_movie(self, mid):
        list1 = []
        if mid in self.movie_names:
            list1.append(self.movie_names[mid])
            list1.append(self.movie_genres[mid])
            return list1
        else:
            return None

    def get_movies(self):
        list_m = []
        for key in self.movie_names:
            list_m.append(int(key))
        return list_m

    def get_all_movies(self):
        movies = list()
        entry = dict()
        m = self.movie_names
        for mid in m:
            entry = dict()
            entry['genres'] = self.movie_genres[int(mid)]
            entry['title'] = self.movie_names[int(mid)]
            entry['result'] = 'success'
            entry['id'] = mid
            if mid in self.imgs:
                entry['img'] = self.imgs[int(mid)]
            else:
                entry['img'] = ""
            movies.append(entry)    
        return movies

    def set_movie(self, mid, update):
        if mid in self.movie_names:
            self.movie_names[mid] = update[0]
            self.movie_genres[mid] = update[1]
        else:
            self.movie_names[mid] = update[0]
            self.movie_genres[mid] = update[1]

    def delete_movie(self, mid):
        if mid in self.movie_names:
            self.movie_names.pop(mid)
            self.movie_genres.pop(mid)

    def load_users(self, users_file):
        ufile = open(users_file, encoding = "ISO-8859-1")
        for user in ufile:
            info = []
            user.strip("\n")
            u = user.split("::")
            uid = int(u[0])
            info.append(u[1])       # gender
            info.append(int(u[2]))  # age
            info.append(int(u[3]))  # occupation
            z = u[4].strip("\n")
            info.append(z)       # zip code
            self.users[int(uid)] = info
        ufile.close()

    def load_images(self, imgs_file):
        ifile = open(imgs_file, encoding = "ISO-8859-1")
        for line in ifile:
            line = line.rstrip("\n")
            line = line.split("::")
            mid = int(line[0])
            f = line[2]
            self.imgs[mid] = f
        ifile.close()
    
    def get_all_users(self):
        u = []
        entry = dict()
        for uid in self.users:
            l = self.users[uid]
            entry = dict()
            entry['zipcode'] = l[3]
            entry['age'] = l[1]
            entry['gender'] = l[0]
            entry['id'] = int(uid)
            if uid == 6029:
                print(entry['gender'])
            entry['occupation'] = l[2]
            u.append(entry)
        return u

    def get_user(self, uid):
        if uid in self.users:
            return self.users.get(uid)
        else:
            return None

    def get_users(self):
        list_u = []
        for uid in self.users:
            list_u.append(int(uid))
        return list_u

    def set_user(self, uid, list_u):
        self.users[uid] = list_u

    def delete_user(self, uid):
        if uid in self.users:
            self.users.pop(uid)

    def load_ratings(self, ratings_file):
        rfile = open(ratings_file, encoding = "ISO-8859-1")
        for line in rfile:
            line = line.split("::")
            self.ratings[int(line[1])] = self.ratings.get(int(line[1]), {})
            self.ratings[int(line[1])].update({int(line[0]):int(line[2].rstrip())})
        rfile.close()
    
    def load_rating_mid(self, ratings_file, mid):
        rfile = open(ratings_file, encoding = "ISO-8859-1")
        for line in rfile:
            line = line.split("::")
            if int(line[1]) == mid:
                self.ratings[int(line[1])] = self.ratings.get(int(line[1]), {})
                self.ratings[int(line[1])].update({int(line[0]):int(line[2].rstrip())})
        rfile.close()

    def get_rating(self, mid):
        tot_rating = 0
        tot_users = 0
        if mid in self.ratings:
            for uid in self.ratings[mid]:
                tot_rating = tot_rating + self.ratings[mid][uid]
                tot_users = tot_users + 1
            return tot_rating/float(tot_users)
        else: 
            return 0
        
    def get_highest_rated_movie(self):
        hrate = 0
        wmid = 0
        if (len(self.ratings) > 0):
            for mid in self.ratings:
                rating = self.get_rating(mid)
                if (rating > hrate):
                    hrate = rating
                    wmid = mid
                elif (rating == hrate):
                    if (mid < wmid):
                        wmid = mid
            return wmid
        else:
            return None

    def get_highest_rated_unvoted_movie(self, uid):
        m = self.movie_names
        maxx = 0
        while m:
            for mid in m:
                rate = self.get_rating(mid)
                if rate > maxx:
                    maxx = rate
                    idd = mid
            if uid is not self.ratings[idd]:
#                print(self.ratings[idd])
#                print(self.get_user_movie_rating(uid, idd))
                return idd
            else:
                m.pop(idd)
        

    def set_user_movie_rating(self, uid, mid, rating):
        self.ratings[mid][uid] = rating

    def get_user_movie_rating(self, uid, mid):
        if mid in self.ratings:
            return self.ratings[mid].get(uid)
    
    def delete_all_ratings(self):
        self.ratings.clear()

if __name__ == "__main__":
       mdb = _movie_database()
       # mdb.load_movies('ml-1m/movies.dat')
       # mdb.load_ratings('ml-1m/ratings.dat')
       # print(mdb.get_highest_rated_movie())

       #### MOVIES ########
        
