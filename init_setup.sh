echo [$(date)]:"START"
echo [$(date)]:"Creating conda env with python 3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)]:"activating env"
source activate ./env
echo [$(date)]:"Initializing dev req."
pip install -r requirements_dev.txt
echo [$(date)]:"END"
