<p align="center">
  <img src="https://i.ibb.co/HTPXt1q/example-prediction.png">
</p>

# Image Supersizer
Image Supersizer is a freely hosted single image super resolution project. Visit the [deployment page](https://thephilosopher.pythonanywhere.com/) to see the current state of the product.

## Model Construction
This project was completed as a capstone poject for my bootcamp at Springboard. See [this repository](https://github.com/salman-a-shah/Springboard) for details about the approach taken to build the model.

## Developer Setup
1. Clone the repo
```
git clone https://github.com/salman-a-shah/image-supersizer.git
```
2. Create a virtual environment
```
python -m venv venv
```
3. Duplicate the file `.env_sample` and rename it to `.env`
4. Edit the `.env` file and set `WORKING_DIRECTORY` as the path to the source folder and set `PYTHON` to the command you'd run in the terminal to run python. This typically is just `python` if you're running a virtual environment, but could be `py -3.7` or whatever version you decide to use. Recommended python version is `3.7.5` since that's the same version as the server, but any `3.6+` version should work fine.
5. Run `app.py`
```
python app.py
```

## Known Issues
Predictions are currently run in the server where only one thread is available. Hence, when one user is running a prediction, the server will be busy and unavailable until the prediction is complete. This issue may or may not be fixed depending on the demand for its use.

## License
[GNU General Public License v3.0](https://github.com/salman-a-shah/image-supersizer/blob/servermaster/LICENSE)
