POPULATION_SIZE = 9
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.1
GLOBA = 1
GLOB = 10000
import sys
import prettytable as prettytable
import random as rnd
import sqlite3 as sqlite

conn = sqlite.connect('class_schedule_4.db')
c = conn.cursor()

class Course:
    def __init__(self, number, name, coursetype, section, instructors, maxNumbOfStudents, tpreference, dpreference, qpreference, ccount, ConflictWith, ConflictValue, rpreference, teacher):
        self._number = number
        self._name = name
        self._coursetype = coursetype
        self._section = section
        self._maxNumbOfStudents = maxNumbOfStudents
        self._instructors = instructors
        self._dpreference = dpreference
        self._qpreference = qpreference
        self._tpreference = tpreference
        self._ccount = ccount
        self._ConflictValue = ConflictValue
        self._ConflictWith = ConflictWith
        self._rpreference = rpreference
        self._teacher = teacher
        #print("helloC")

    def get_number(self):
        return self._number

    def get_name(self):
        return self._name

    def get_instructors(self):
        return self._instructors

    def get_maxNumbOfStudents(self):
        return self._maxNumbOfStudents

    def get_section(self):
        return self._section

    def get_coursetype(self):
        return self._coursetype

    def get_dpreference(self):
        return self._dpreference

    def get_qpreference(self):
        return self._qpreference

    def get_tpreference(self):
        return self._tpreference

    def get_ccount(self):
        return self._ccount

    def set_ccount(self, c):
        self._ccount = c

    def get_ConflictWith(self):
        return self._ConflictWith

    def set_ConflictWith(self, c):
        self._ConflictWith = c

    def get_ConflictValue(self):
        return self._ConflictValue

    def set_ConflictValue(self, c):
        self._ConflictValue = c

    def get_rpreference(self):
        return self._rpreference

    def get_teacher(self):
        return self._teacher

    def __str__(self):
        return self._name


class Department:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses
        #print("helloD")

    def get_name(self):
        return self._name

    def get_courses(self):
        return self._courses


class Instructor:
    def __init__(self, id, name, spacer, spacercheck):
        self._id = id
        self._name = name
        self._spacer = spacer
        self._spacerc = spacercheck
        #print("helloI")

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_spacer(self):
        return self._spacer

    def get_spacerc(self):
        return self._spacerc

    def get_spacercc(self):
        self._spacerc = 1

    def __str__(self):
        return self._name


class MeetingTime:
    def __init__(self, id, time, check, matcher):
        self._id = id
        self._time = time
        self._check = check
        self._matcher = matcher
        #print("helloM")

    def get_id(self):
        return self._id

    def get_time(self):
        return self._time

    def get_check(self):
        return self._check

    def get_matcher(self):
        return self._matcher


class Room:
    def __init__(self, number, roomtype, seatingCapacity):
        self._number = number
        self._roomtype = roomtype
        self._seatingCapacity = seatingCapacity
        #print("helloR")
        # print(number)
        # print(seatingCapacity)

    def get_number(self):
        return self._number

    def get_roomtype(self):
        return self._roomtype

    def get_seatingCapacity(self):
        return self._seatingCapacity


class Class:
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._instructor = None
        self._meetingTime = None
        self._room = None
        #print("in class")
        #print(type(self._room))

    def get_id(self):
        return self._id

    def get_dept(self):
        return self._dept

    def get_course(self):
        return self._course

    def get_instructor(self):
        return self._instructor

    def get_meetingTime(self):
        return self._meetingTime

    def get_room(self):
        return self._room

    def set_instructor(self, instructor):
        self._instructor = instructor
        #print("in instructor")

    def set_meetingTime(self, meetingTime):
        #print("in meeting")
        self._meetingTime = meetingTime


    def set_room(self, room):
        self._room = room


    def __str__(self):
        return str(self._dept.get_name()) + "," + str(self._course.get_number()) + "," + str(
            self._room.get_number()) + "," + str(self._instructor.get_id()) + "," + str(self._meetingTime.get_id())


class DBMgr:
    def __init__(self):
        self._rooms = self.select_rooms()
        self._meetingTimes = self.select_meeting_times()
        self._instructors = self.select_instructors()
        self._courses = self.select_courses()
        self._depts = self.select_depts()
        self._numberOfClasses = 0
        #print("hamzaaa")
        for i in range (0, len(self._depts)):
            self._numberOfClasses += len(self._depts[i].get_courses())

    def select_rooms(self):
        c.execute("SELECT * FROM room")
        rooms = c.fetchall()
        returnRooms = []
        for i in range(0, len(rooms)):
            returnRooms.append(Room(rooms[i][0], rooms[i][1], rooms[i][2]))

        return returnRooms


    def select_meeting_times(self):
        c.execute("SELECT * FROM meeting_time")
        meetingTimes = c.fetchall()
        returnMeetingTimes = []
        for i in range (0, len(meetingTimes)):
            returnMeetingTimes.append(MeetingTime(meetingTimes[i][0], meetingTimes[i][1], meetingTimes[i][2], meetingTimes[i][3]))

        return returnMeetingTimes


    def select_instructors(self):
        c.execute("SELECT * FROM instructor")
        instructors = c.fetchall()
        returnInstructors = []
        for i in range (0, len(instructors)):
            returnInstructors.append(Instructor(instructors[i][0], instructors[i][1], instructors[i][2], instructors[i][3]))

        return returnInstructors



    def select_courses(self):
        c.execute("SELECT * FROM course")
        courses = c.fetchall()
        returnCourses = []
        for i in range (0, len(courses)):
            returnCourses.append(Course(courses[i][0], courses[i][1], courses[i][2], courses[i][3], self.select_course_instructors(courses[i][0]) , courses[i][4], courses[i][5], courses[i][6], courses[i][7], courses[i][8], courses[i][9], courses[i][10], courses[i][11], courses[i][12])) #self.select_course_instructors(courses)
        return returnCourses


    def select_depts(self):
        c.execute("SELECT * FROM dept")
        #print("In depts")
        depts = c.fetchall()
        returnDepts = []
        for i in range(0, len(depts)):
            returnDepts.append(Department(depts[i][0], self.select_dept_courses(depts[i][0])))
        return returnDepts


    def select_course_instructors(self, courseNumber):
        c.execute("SELECT * FROM course_instructor where course_number = ?" ,(courseNumber,) )
        dbInstructorNumbers = c.fetchall()
        instructorNumbers = []

        for i in range(0, len(dbInstructorNumbers)):
            instructorNumbers.append(dbInstructorNumbers[i][1])
        returnValue = []

        for i in range (0, len(self._instructors)):
            if self._instructors[i].get_id() in instructorNumbers:
                returnValue.append(self._instructors[i])
        return returnValue



    def select_dept_courses(self, deptName):
        c.execute("SELECT * FROM dept_course where name == '" + deptName + "'")
        dbCourseNumbers = c.fetchall()
        courseNumbers = []

        for i in range(0, len(dbCourseNumbers)):
            courseNumbers.append(dbCourseNumbers[i][1])
        returnValue = []

        for i in range (0, len(self._courses)):
            if self._courses[i].get_number() in courseNumbers:
                returnValue.append(self._courses[i])
        return returnValue


    def get_rooms(self):
        return self._rooms

    def get_instructors(self):
        return self._instructors

    def get_courses(self):
        return self._courses

    def get_depts(self):
        return self._depts

    def get_meetingTimes(self):
        return self._meetingTimes

    def get_numberOfClasses(self):
        return self._numberOfClasses


class Schedule:
    def __init__(self):
        self._data = data
        self._classes = []
        self._numbOfConflicts = 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True

    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes

    def get_numbOfConflicts(self):
        return self._numbOfConflicts

    def get_fitness(self):
        if (self._isFitnessChanged == True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness

    @property
    def initialize(self):
        depts = self._data.get_depts()
        classes0 = self.get_classes()
        for i in range(0, len(depts)):
            courses = depts[i].get_courses()
            for j in range(0, len(courses)):
                newClass = Class(self._classNumb, depts[i], courses[j])

                self._classNumb += 1
                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(0, len(data.get_meetingTimes()))])
                op = newClass.get_course().get_rpreference()
                if(op == 'N/A'):
                    newClass.set_room(data.get_rooms()[rnd.randrange(0, (len(data.get_rooms()) - 9))])
                    #breakpoint()
                else:
                    for m in range(26):
                        if ((data.get_rooms()[m].get_number()) == op):
                            newClass.set_room(data.get_rooms()[m])
                            #breakpoint()

                newClass.set_instructor(courses[j].get_instructors()[rnd.randrange(0, len(courses[j].get_instructors()))])

                if ((newClass.get_course().get_tpreference()) == 1 ):
                        if ((newClass.get_course().get_dpreference()) == 1 ):
                            if((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(0, (len(data.get_meetingTimes())) - 126)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(5, (len(data.get_meetingTimes())) - 122)])


                        if ((newClass.get_course().get_dpreference()) == 2 ):
                            if ((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(9, (len(data.get_meetingTimes())) - 117)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(14, (len(data.get_meetingTimes())) - 113)])
                            #newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(8, (len(data.get_meetingTimes()))-8)])


                        if ((newClass.get_course().get_dpreference()) == 3 ):
                            if((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(18, (len(data.get_meetingTimes())) - 108)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(23, (len(data.get_meetingTimes())) - 104)])

                        if ((newClass.get_course().get_dpreference()) == 4 ):
                            if ((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(51, (len(data.get_meetingTimes())) - 75)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(56, (len(data.get_meetingTimes())) - 71)])

                        if ((newClass.get_course().get_dpreference()) == 5 ):
                            if ((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(95, (len(data.get_meetingTimes())) - 31)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(100, (len(data.get_meetingTimes())) - 27)])


                        if ((newClass.get_course().get_dpreference()) == 6 ): #hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                            if((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(122, (len(data.get_meetingTimes())) - 4)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(127, (len(data.get_meetingTimes())))])

                if ((newClass.get_course().get_tpreference()) == 1.5 ):
                        if ((newClass.get_course().get_dpreference()) == 1 ):
                            if((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(27, (len(data.get_meetingTimes())) - 101)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(30, (len(data.get_meetingTimes())) - 98)])

                        if ((newClass.get_course().get_dpreference()) == 2 ):
                            if ((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(33, (len(data.get_meetingTimes())) - 95)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(36, (len(data.get_meetingTimes())) - 92)])


                        if ((newClass.get_course().get_dpreference()) == 3 ):
                            if ((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(39, (len(data.get_meetingTimes())) - 89)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(42, (len(data.get_meetingTimes())) - 86)])


                        if ((newClass.get_course().get_dpreference()) == 4 ):
                            if ((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(45, (len(data.get_meetingTimes())) - 83)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(48, (len(data.get_meetingTimes())) - 80)])

                        if ((newClass.get_course().get_dpreference()) == 5 ):
                            if ((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(104, (len(data.get_meetingTimes())) - 24)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(107, len(data.get_meetingTimes())) - 21])

                if ((newClass.get_course().get_tpreference()) == 2 ):
                        if ((newClass.get_course().get_dpreference()) == 1 ):
                            if((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(60, (len(data.get_meetingTimes())) - 69)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(62, (len(data.get_meetingTimes())) - 67)])


                        if ((newClass.get_course().get_dpreference()) == 2 ):
                            if ((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(64, (len(data.get_meetingTimes())) - 65)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(66, (len(data.get_meetingTimes())) - 63)])
                            #newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(8, (len(data.get_meetingTimes()))-8)])


                        if ((newClass.get_course().get_dpreference()) == 3 ):
                            if((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(68, (len(data.get_meetingTimes())) - 61)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(70, (len(data.get_meetingTimes())) - 59)])

                        if ((newClass.get_course().get_dpreference()) == 4 ):
                            if ((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(72, (len(data.get_meetingTimes())) - 57)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(74, (len(data.get_meetingTimes())) - 55)])

                        if ((newClass.get_course().get_dpreference()) == 5 ):
                            if ((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(76, (len(data.get_meetingTimes())) - 53)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(78, (len(data.get_meetingTimes())) - 51)])

                if ((newClass.get_course().get_tpreference()) == 3):
                        newClass.set_room(data.get_rooms()[rnd.randrange(17, (len(data.get_rooms())))])
                        if ((newClass.get_course().get_dpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(80, (len(data.get_meetingTimes())) - 48)])


                        if ((newClass.get_course().get_dpreference()) == 2):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(83, (len(data.get_meetingTimes())) - 45)])


                        if ((newClass.get_course().get_dpreference()) == 3):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(86, (len(data.get_meetingTimes())) - 42)])


                        if ((newClass.get_course().get_dpreference()) == 4):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(89, (len(data.get_meetingTimes())) - 39)])


                        if ((newClass.get_course().get_dpreference()) == 5):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(92, (len(data.get_meetingTimes())) - 36)])

                if ((newClass.get_course().get_tpreference()) == 4 ):
                        if ((newClass.get_course().get_dpreference()) == 1 ):
                            if((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(110, (len(data.get_meetingTimes())) - 19)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(112, (len(data.get_meetingTimes())) - 17)])


                        if ((newClass.get_course().get_dpreference()) == 2 ):
                            if ((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(114, (len(data.get_meetingTimes())) - 15)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(116, (len(data.get_meetingTimes())) - 13)])
                            #newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(8, (len(data.get_meetingTimes()))-8)])


                        if ((newClass.get_course().get_dpreference()) == 3 ):
                            if((newClass.get_course().get_qpreference()) == 1):
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(118, (len(data.get_meetingTimes())) - 11)])
                            else:
                                newClass.set_meetingTime(data.get_meetingTimes()[rnd.randrange(120, (len(data.get_meetingTimes())) - 9)])


                self._classes.append(newClass)

        return self

    def calculate_fitness(self):
        self._numbOfConflicts = 0
        w = "OK"
        classes = self.get_classes()
        for i in range(0, len(classes)):
            if (classes[i].get_room().get_seatingCapacity() < classes[i].get_course().get_maxNumbOfStudents()):
                self._numbOfConflicts += 1
            for j in range(0, len(classes)):
                if (j >= i):
                    if (classes[i].get_instructor() == classes[j].get_instructor()):
                        if (classes[i].get_instructor().get_spacer() == 1):
                            if (classes[i].get_instructor().get_spacerc() == 0):
                                if ((classes[i].get_meetingTime().get_matcher() - classes[j].get_meetingTime().get_matcher()) == 1 or (classes[i].get_meetingTime().get_matcher() - classes[j].get_meetingTime().get_matcher()) == -1):
                                    #self._numbOfConflicts += 1
                                    c.execute("select status from course_timing where CourseName = '" + str( classes[i].get_course().get_name()) + "' ")
                                    g = str(c.fetchall())

                                    q = classes[i].get_course().get_ccount()
                                    # print(q)

                                    if ((g != "[(' A ',)]") and (q < 10000)):
                                        y = str(classes[i].get_course().get_name())
                                        z1 = str(classes[i].get_meetingTime().get_time())
                                        gg = "OK "
                                        c.execute("update course_timing set status = '" + gg + "' where CourseName = '" + y + "'")
                                        self._numbOfConflicts += 1
                                        q = q + 1
                                        classes[i].get_course().set_ccount(q)
                                        # breakpoint()
                                    elif (q == 10000):
                                        q = q + 1
                                        classes[i].get_course().set_ccount(q)
                                        l = str(classes[j].get_course().get_name())
                                        z = str(classes[i].get_meetingTime().get_time()) + " (Consecutive Classes Clash)"
                                        classes[i].get_course().set_ConflictWith(l)
                                        classes[i].get_course().set_ConflictValue(z)

                                    elif (q < 10000):
                                        q = q + 1
                                        classes[i].get_course().set_ccount(q)
                                        self._numbOfConflicts += 1
                                    else:
                                        p = 1
                                    self._numbOfConflicts += 1

                    if (classes[i].get_meetingTime() == classes[j].get_meetingTime() and classes[i].get_id() != classes[j].get_id()):
                        if (classes[i].get_room() == classes[j].get_room()):
                            c.execute("select status from course_timing where CourseName = '" + str(classes[i].get_course().get_name()) + "' ")
                            g = str(c.fetchall())

                            q = classes[i].get_course().get_ccount()

                            if ((g != "[(' A ',)]") and (q < 10000)):
                                y = str(classes[i].get_course().get_name())
                                z1 = str(classes[i].get_meetingTime().get_time())
                                gg = "OK "
                                c.execute("update course_timing set status = '" + gg + "' where CourseName = '" + y + "'")
                                self._numbOfConflicts += 1
                                q = q + 1
                                classes[i].get_course().set_ccount(q)
                            elif (q == 10000):
                                q = q + 1
                                classes[i].get_course().set_ccount(q)
                                l = str(classes[j].get_course().get_name())
                                z = str(classes[i].get_meetingTime().get_time()) + " (Room Conflict)"
                                classes[i].get_course().set_ConflictWith(l)
                                classes[i].get_course().set_ConflictValue(z)

                            elif (q < 10000):
                                q = q + 1
                                classes[i].get_course().set_ccount(q)
                                self._numbOfConflicts += 1
                            else:
                                p = 1
                            self._numbOfConflicts += 1
                        if (classes[i].get_instructor() == classes[j].get_instructor()):
                            c.execute("select status from course_timing where CourseName = '" + str(classes[i].get_course().get_name()) + "' ")
                            g = str(c.fetchall())
                            q = classes[i].get_course().get_ccount()

                            if ((g != "[(' A ',)]") and (q < 10000)):
                                y = str(classes[i].get_course().get_name())
                                z1 = str(classes[i].get_meetingTime().get_time())
                                gg = "OK "
                                c.execute("update course_timing set status = '" + gg + "' where CourseName = '" + y + "'")
                                self._numbOfConflicts += 1
                                q = q + 1
                                classes[i].get_course().set_ccount(q)
                            elif (q == 10000):
                                q = q+1
                                classes[i].get_course().set_ccount(q)
                                l = str(classes[j].get_course().get_name())
                                z = str(classes[i].get_meetingTime().get_time()) + " (Instructor Conflict)"
                                classes[i].get_course().set_ConflictWith(l)
                                classes[i].get_course().set_ConflictValue(z)

                            elif (q < 10000):
                                q = q + 1
                                classes[i].get_course().set_ccount(q)
                                self._numbOfConflicts += 1
                            else:
                                p = 1

                        if (classes[i].get_course().get_section() == classes[j].get_course().get_section()):
                            c.execute("select status from course_timing where CourseName = '" + str(classes[i].get_course().get_name()) + "' ")
                            g = str(c.fetchall())
                            q = classes[i].get_course().get_ccount()

                            if ((g != "[(' A ',)]") and (q < 10000)):
                                y = str(classes[i].get_course().get_name())
                                z1 = str(classes[i].get_meetingTime().get_time())
                                gg = "OK "
                                c.execute("update course_timing set status = '" + gg + "' where CourseName = '" + y + "'")
                                self._numbOfConflicts += 1
                                q = q + 1
                                classes[i].get_course().set_ccount(q)

                            elif ((q == 10000) ): #or (q == 1001) or (q == 1000)
                                q = q + 1
                                classes[i].get_course().set_ccount(q)
                                l = str(classes[j].get_course().get_name())
                                z = str(classes[i].get_meetingTime().get_time())
                                classes[i].get_course().set_ConflictWith(l)
                                classes[i].get_course().set_ConflictValue(z)

                            elif (q < 10000):
                                q = q + 1
                                classes[i].get_course().set_ccount(q)
                                self._numbOfConflicts += 1
                            else:
                                p = 1

            t = str(classes[i].get_meetingTime().get_time())
            u = str(classes[i].get_instructor().get_name())
            v = str(classes[i].get_room().get_number())
            y = str(classes[i].get_course().get_name())
            if((classes[i].get_course().get_ccount()) == 10001):
                r1 = classes[i].get_course().get_ConflictWith()
                z1 = classes[i].get_course().get_ConflictValue()
                status = "Conflict Exist with " + r1 + "at Value: " + z1

            else:
                status = "No Conflicts!"
            c.execute("update course_timing set timing = '" + t + "', teacher = '" + u + "', room = '" + v + "', status = '" + status + "' where CourseName = '" + y + "'") #, status = '" + w + "'
        #print(self._numbOfConflicts)
        return 1 / ((1.0 * self._numbOfConflicts + 1))

    def __str__(self):
        returnValue = ""
        for i in range(0, len(self._classes) - 1):
            returnValue += str(self._classes[i]) + " , "
        returnValue += str(self._classes[len(self._classes) - 1])
        return returnValue


class Population():
    def __init__(self, size):
        self._size = size
        self._data = data
        self._schedules = []
        for i in range(0, size):
            self._schedules.append(Schedule().initialize)

    def get_schedules(self):
        return self._schedules


class DisplayMgr:
    def print_available_data(self):
        print("> All Available Data")
        self.print_dept()
        self.print_course()
        self.print_room()
        self.print_instructor()
        #self.print_meeting_times()

    def print_dept(self):
        depts = data.get_depts()
        availableDeptsTable = prettytable.PrettyTable(['Dept', 'Courses'])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_courses()
            tempStr = "["
            for j in range(0, len(courses) - 1):
                tempStr += courses[j].__str__() + ", "
            tempStr += courses[len(courses) - 1].__str__() + "]"
            availableDeptsTable.add_row([depts.__getitem__(i).get_name(), tempStr])
        print(availableDeptsTable)

    def print_course(self):
        availableCoursesTable = prettytable.PrettyTable(['CourseID', 'Course Name', 'Max No. of students', 'Instructors'])
        courses = data.get_courses()
        for i in range(0, len(courses)):
            instructors = courses[i].get_instructors()
            tempStr = ""
            #print("in print", courses[i], instructors, len(instructors))
            for j in range(0, len(instructors) - 1):
                tempStr += instructors[j].__str__() + ","
                #print("in str")
                #print(tempStr)
            tempStr += instructors[len(instructors) - 1].__str__()
            availableCoursesTable.add_row([courses[i].get_number(), courses[i].get_name(), str(courses[i].get_maxNumbOfStudents()), tempStr])
        print(availableCoursesTable)

    def print_instructor(self):
        availableInstructorsTable = prettytable.PrettyTable(['InstructorID', 'Instructor'])
        instructors = data.get_instructors()
        for i in range(0, len(instructors)):
            availableInstructorsTable.add_row([instructors[i].get_id(), instructors[i].get_name()])
        print(availableInstructorsTable)

    def print_room(self):
        availableRoomsTable = prettytable.PrettyTable(['Room Number', 'Max Seating Capacity'])
        rooms = data.get_rooms()
        for i in range(0, len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].get_number()), str(rooms[i].get_seatingCapacity())])
        print(availableRoomsTable)

    def print_meeting_times(self):
        availableMeetingTimeTable = prettytable.PrettyTable(['ID', 'Meeting Time'])
        meetingTimes = data.get_meetingTimes()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row([meetingTimes[i].get_id(), meetingTimes[i].get_time()])
        print(availableMeetingTimeTable)

    def print_generation(self, population):
        table1 = prettytable.PrettyTable(['Schedule Number', 'Fitness', 'No. of conflicts', 'Class[Dept,Class,Room,Instructor]'])
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table1.add_row([str(i+1), round(schedules[i].get_fitness(), 3), schedules[i].get_numbOfConflicts(), schedules[i].__str__() ])
        print(table1)

    def print_schedule_as_table(self, schedule):
        classes = schedule.get_classes()

        table = prettytable.PrettyTable(['Class Number', 'Dept', 'Course ( Max No. of Students)', 'Room(Capacity)', 'Instructor(ID)', 'Time (ID)', 'P'])
        for i in range(0, len(classes)):
            table.add_row([str(i+1), classes[i].get_dept().get_name(), classes[i].get_course().get_name() + "(" + str(classes[i].get_course().get_maxNumbOfStudents()) + ")",
                           classes[i].get_room().get_number() + " (" +str(classes[i].get_room().get_seatingCapacity()) + ")",
                           classes[i].get_instructor().get_name() + " (" +str(classes[i].get_instructor().get_id()) + ")",
                           classes[i].get_meetingTime().get_time() + " (" + str(classes[i].get_meetingTime().get_id()) + ")" , classes[i].get_course().get_ccount()])

        print(table)


class GeneticAlgorithm:
    def evolve(self, population): #
        return self._mutate_population(self._crossover_population(population))

    def _crossover_population(self, pop): # Does crossover on all Schedules of the population
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_SCHEDULES):
            crossover_pop.get_schedules().append(pop.get_schedules()[i])
        i = NUMB_OF_ELITE_SCHEDULES
        while i < POPULATION_SIZE:
            schedule1 = self._select_tournament_population(pop).get_schedules()[0]
            schedule2 = self._select_tournament_population(pop).get_schedules()[0]
            crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
            i += 1
        return crossover_pop

    def _mutate_population(self, population): # Does mutation on all Schedules of the population
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
        return population

    def _crossover_schedule(self, schedule1,schedule2): # Does Crossover on 2 Schedules that were selected in STP
        crossoverSchedule = Schedule().initialize
        for i in range(0, len(crossoverSchedule.get_classes())):
            if(rnd.random() > 0.5):
                crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else:
                crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
        return crossoverSchedule

    def _mutate_schedule(self, mutateSchedule): # Called by MP
        schedule = Schedule().initialize
        for i in range(0, len(mutateSchedule.get_classes())):
            if(MUTATION_RATE > rnd.random()):
                mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
        return mutateSchedule


    def _select_tournament_population(self,pop):  #Select 2 Schedules to do crossover on
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop



data = DBMgr()
displayMgr = DisplayMgr()
displayMgr.print_available_data()
generationNumber = 0
print("\n> Generation # " + str(generationNumber))
population = Population(POPULATION_SIZE)

# print(type(population.get_schedules().get_classes()))
# print("absd")
# classes[i].get_room().get_seatingCapacity() )
population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)  # Sorts the schedule and population
displayMgr.print_generation(population)  # Prints G0
displayMgr.print_schedule_as_table(population.get_schedules()[0])  # Prints the fittest schedule in that generation
geneticAlgorithm = GeneticAlgorithm()
while (population.get_schedules()[0].get_fitness() != 1.0 and GLOBA<GLOB):
    if(population.get_schedules()[0].get_fitness() == 0.5):
        print()
    generationNumber += 1
    GLOBA = GLOBA+1
    print("\n> Generation # " + str(generationNumber))
    population = geneticAlgorithm.evolve(population)
    population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
    displayMgr.print_generation(population)
    displayMgr.print_schedule_as_table(population.get_schedules()[0])

print("\n\n")

conn.commit()

conn.close()
