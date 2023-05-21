"""Philosopher class that sets up model and has functions for
giving responses and updating weights given other responses."""

from our_new_community.reward import *
from our_new_community.models import load_model, load_tokenizer


class Philosopher():
    def __init__(self, config):
        """Load a philosopher model with the right components
        to participate in our discussions."""

        self.name = config['name']
        self.model_name = config['model_name']
        self.model_type = config['model_type']

        self.model, self.context_len = load_model(self.model_name,
                                                  self.model_type)
        self.tokenizer = load_tokenizer(self.model)


    def get_response(self, prompt):
        """Get a response from the philosopher given a prompt."""

        prompt += f"\n{self.model_name}: "
        response = some_stuff
        return response


    def update_weights(self, response):
        """Given a response from another philosopher, update the
        original philosopher's weights."""

        """Do RLHF stuff"""