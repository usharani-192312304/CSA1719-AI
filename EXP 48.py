from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create Bayesian Network
model = DiscreteBayesianNetwork([
    ('Rain', 'WetGrass'),
    ('Sprinkler', 'WetGrass')
])

# Define probability distributions
cpd_rain = TabularCPD(
    variable='Rain',
    variable_card=2,
    values=[[0.8], [0.2]]
)

cpd_sprinkler = TabularCPD(
    variable='Sprinkler',
    variable_card=2,
    values=[[0.5], [0.5]]
)

cpd_wetgrass = TabularCPD(
    variable='WetGrass',
    variable_card=2,
    values=[
        [0.99, 0.10, 0.10, 0.01],
        [0.01, 0.90, 0.90, 0.99]
    ],
    evidence=['Rain', 'Sprinkler'],
    evidence_card=[2, 2]
)

# Add probability distributions
model.add_cpds(cpd_rain, cpd_sprinkler, cpd_wetgrass)

# Check model
print("Model Valid:", model.check_model())

# Perform probabilistic inference
inference = VariableElimination(model)

result = inference.query(
    variables=['WetGrass'],
    evidence={'Rain': 1}
)

print("\nProbability of Wet Grass when it rains:")
print(result)
