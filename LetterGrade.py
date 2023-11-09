from sqlalchemy import Date, ForeignKey
from sqlalchemy import UniqueConstraint, ForeignKeyConstraint, CheckConstraint
from sqlalchemy.orm import mapped_column, Mapped
from Enrollment import Enrollment
from sqlalchemy import String


class LetterGrade(Enrollment):
    __tablename__ = "letter_grade"
    letterGradeId: Mapped[int] = mapped_column('letter_grade_id',
                                               ForeignKey("enrollments.enrollment_id",
                                                          ondelete="CASCADE"), primary_key=True)
    applicationDate: Mapped[Date] = mapped_column('application_date', Date, nullable=False)
    grade: Mapped[str] = mapped_column('grade', String(1), CheckConstraint("grade IN('A', 'B', 'C', 'D', 'F')",
                                                                           name="enrollment_grade_constraint"),
                                       nullable=False)

    __mapper_args__ = {"polymorphic_identity": "pass_fail"}

    def __init__(self, section, student, application_date: Date, grade: String):
        super().__init__(section, student)
        self.applicationDate = application_date
        self.grade = grade

    def __str__(self):
        return f"LetterGrade Enrollment: {super().__str__()}"

#5gAg$v$H