from cdclassifier.config.configuration import ConfigurationManager
from cdclassifier.components.model_evaluation import Evaluation
from cdclassifier import logger

STAGE_NAME = "Model Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(config=val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__ == "__main__":
    try:
        logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x')
    
    except Exception as e:
        logger.exception(e)
        raise e
    