echo "Installing chord_drs"

if [ -d chord_drs_venv ]; then
    echo "Found previous Chord DRS virtual environment. Deleting it.";
    rm -f -r chord_drs_venv;
fi

echo "Creating virtual environment for Chord DRS"; 
python3 -m venv chord_drs_venv
cd chord_drs_venv
source bin/activate
echo "Cloning chord_dr repository"
git clone https://github.com/c3g/chord_drs.git
cd chord_drs
echo "Installing requirements"
pip install -r requirements.txt
flask db upgrade
echo "Starting Chord DRS service."
python ../../scripts/run_chord_drs.py
