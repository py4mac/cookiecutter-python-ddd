from sqlalchemy import Column, Float, Integer, String, DateTime, PrimaryKeyConstraint, CheckConstraint, Index
import datetime
from {{cookiecutter.app_name}}.store.db.sql_database import db
from {{cookiecutter.app_name}}.entities.experiment import ExperimentAction, ExperimentState

ActionTypes = [
    ExperimentAction.NONE,
    ExperimentAction.FORWARD,
    ExperimentAction.BACKWARD,
    ExperimentAction.LEFT,
    ExperimentAction.RIGHT
]

StateTypes = [
    ExperimentState.STOPPED,
    ExperimentState.FAILED,
    ExperimentState.RUNNING,
    ExperimentState.FINISHED,
]


class Experiment(db.BaseModel):  # type: ignore
    id = Column(Integer, autoincrement=True)
    experiment_uuid = Column(String(32), nullable=False)
    ts = Column(DateTime, default=str(datetime.now()))
    action = Column(String(32), default="none")
    vision_sensor = Column(Float, nullable=True)
    speed = Column(Float, nullable=True)
    state = Column(String(32), default="stopped")

    __table_args__ = (
        PrimaryKeyConstraint("id", name="experiment_pk"),
        CheckConstraint(action.in_(ActionTypes), name="experiment_checkaction"),
        CheckConstraint(state.in_(StateTypes), name="experiment_checkstate"),
        Index("experiment_index1", "experiment_uuid"),
    )

    def __repr__(self):
        return "<Experiment ({}, {})>".format(self.experiment_uuid, self.ts, self.action, self.vision_sensor, self.speed, self.state)
