import re
import pandas as pd
import itertools
import collections
import matplotlib.pyplot as plt
import lightgbm as lgb
#import train test split module
from sklearn.model_selection import train_test_split
from django.contrib.admin.templatetags.admin_list import results
from django.views import View
from django.contrib.auth.hashers import check_password, make_password
from Recommendation.models.collegereview import Review
from django.views import View
pattern = re.compile(r'')
from django.shortcuts import render, redirect
from Recommendation.models.collegereview import Review
from Recommendation.models.faculty import Faculty

class postReview(View):
    def get(self, request):
        results = Faculty.objects.all()
        return render(request, 'review.html', {'showFaculty': results})

    def post(self, request):
        postData = request.POST
        schoolname = postData.get('schoolname')
        schoollocation = postData.get('schoollocation')
        registered_email = request.session.get('email')
        collegeName = postData.get('collegeName')
        collegeLocation = postData.get('collegeLocation')
        faculty = postData.get('faculty')
        reviews = postData.get('review')
        review = pd.read_csv('IMDB Dataset.csv')
        print(review)
        # stopwords library from nltk package
        from nltk.corpus import stopwords
        # extracting english stopwords frm nltk package
        stop_words = set(stopwords.words('english'))
        # converting Set stopwords to list
        stop_word_list = list(stop_words)

        # function for preprocessing our reviews
        def preprocess_text(corpus):
            # converting everything into lower case
            corpus['review'] = corpus['review'].str.lower()
            # removing urls from the reviews using regular expressions(regex)
            corpus['review'] = corpus['review'].str.replace(r"http\S+", "", regex=True)
            # removing everything except alphabets and numbers from reviews
            corpus['review'] = corpus['review'].str.replace('[^A-Za-z0-9]+', ' ', regex=True)
            # removing stopwords(frequently occuring words) like a, and, the , are which has no significance in our review analysis
            corpus['review'] = corpus['review'].apply(
                lambda words: ' '.join(word.lower() for word in words.split() if word not in stop_word_list))
            return corpus

        review_data = preprocess_text(review)
        # import nltk library
        import nltk
        # download wordnet and punkt package from nltk, it will be required for tokenization and lemmatization
        nltk.download('wordnet')
        nltk.download('punkt')
        # intializing tokenizer object
        w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
        # initializing lemmatizer object
        lemmatizer = nltk.stem.WordNetLemmatizer()

        # function for tokenizing and lemmatizing reviews
        def lemmatize_text(review):
            return [lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(review)]

        # applying the above function
        review_data['lemmatized_tokens'] = review_data['review'].apply(lemmatize_text)
        # viewing the updated reviews dataframe
        lemmatized_tokens = list(review_data['lemmatized_tokens'])
        token_list = list(itertools.chain(*lemmatized_tokens))
        count_no = collections.Counter(token_list)
        clean_reviews = pd.DataFrame(count_no.most_common(30), columns=['words', 'count'])
        fig, ax = plt.subplots(figsize=(12, 8))
        clean_reviews.sort_values(by='count').plot.barh(x='words', y='count', ax=ax, color="green")
        ax.set_title("Most frequently used words in reviews")
        bigrams = zip(token_list, token_list[1:])
        count_no = collections.Counter(bigrams)

        clean_reviews = pd.DataFrame(count_no.most_common(30), columns=['words', 'count'])
        fig, ax = plt.subplots(figsize=(12, 8))
        clean_reviews.sort_values(by='count').plot.barh(x='words', y='count', ax=ax, color="green")
        from sklearn.feature_extraction.text import TfidfVectorizer
        tfidf_vectorizer = TfidfVectorizer(max_features=2000)
        # extracting features using tfidf in array format
        features = tfidf_vectorizer.fit_transform(review_data['review']).toarray()
        review_data = preprocess_text(review)
        target = review_data['sentiment']
        # splitting training data to train and test
        x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.25)
        # initializing model with hyperparameters, read documentation of the model for more details on hyperparameters
        clf = lgb.LGBMClassifier(max_depth=20, n_estimators=25, min_child_weight=0.0016, n_jobs=-1)
        # apply the training input and output for model to learn
        clf.fit(x_train, y_train)
        # obj = request.session['review']
        obj = request.POST.get('review')
        pred = clf.predict(tfidf_vectorizer.transform([obj]))
        # save_ReviewResult = Review(
        #     Review_result=pred,
        # )
        # save_ReviewResult.ReviewResult()
        # request.session['review'] = 'This is loving college'
        rating = postData.get('rating')
        print("The review rating",rating)
        # facultyInstance = Faculty.objects.get(pk=faculty)
        # validation
        addReview = Review(
                            oldschool = schoolname,
                            schoollocation = schoollocation,
                            registered_email = registered_email,
                            collegeName=collegeName,
                            collegeLocation=collegeLocation,
                            facultyName_id=faculty,
                            collegeReview=reviews,
                            Review_result=pred,
                            rating = rating)
        Review_error = self.validateReview(schoolname,schoollocation,collegeName, collegeLocation, addReview)
        value = {
            'schoolName':schoolname,
            'schoolLocation':schoollocation,
            'collegeName': collegeName,
            'collegeLocation': collegeLocation,
            }

        if not Review_error:
            addReview.AddReview()
            return redirect('DashboardHome')
        else:
            reviewdata = {
                'error': Review_error,
                'values': value,
                'showFaculty': results
            }
        return render(request, 'review.html', reviewdata)
    def validateReview(self,schoolName,schoolLocation,collegeName, collegeLocation,collegereview):
        Review_error = None
        if not schoolName:
            Review_error = "School name should be added"
        elif re.search(r'[A-Z]', schoolName):
            Review_error = "school name donot contain capital letter"

        if not schoolLocation:
            Review_error = "school name should be added"
        elif re.search(r'[A-Z]', schoolLocation):
            Review_error = "schoolocation name donot contain capital letter"
        if not collegeName:
            Review_error = "College name should be added"
        elif re.search(r'[A-Z]', collegeName):
            Review_error = "College name donot contain capital letter"
        elif re.search(r'[A-Z]', collegeLocation):
            Review_error = "college Location doesnot contain capital letter"
        elif collegereview.isExist:
            Review_error = "This Email already gave Review"

        # elif addReview.isExist():
    #       Review_error = 'Email Address Already Registered'
        return Review_error
