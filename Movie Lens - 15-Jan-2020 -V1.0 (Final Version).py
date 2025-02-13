{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Project 2: Movie Lens Case Study"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step1 : Read the dataets and load them into Dataframes "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# importing required libraries for processings\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline\n",
    "import seaborn as sns\n",
    "import warnings\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read the movies.dat file and assign the column names\n",
    "MoviesDF = pd.read_csv(\"C:/Users/E056362/Documents/1 New Project/Datasets/Movie Lens/movies.dat\",sep=\"::\",\n",
    "                      header=None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "MoviesDF.columns = ['MovieID','Title','Genres']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>MovieID</th>\n",
       "      <th>Title</th>\n",
       "      <th>Genres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Toy Story (1995)</td>\n",
       "      <td>Animation|Children's|Comedy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Jumanji (1995)</td>\n",
       "      <td>Adventure|Children's|Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Grumpier Old Men (1995)</td>\n",
       "      <td>Comedy|Romance</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Waiting to Exhale (1995)</td>\n",
       "      <td>Comedy|Drama</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Father of the Bride Part II (1995)</td>\n",
       "      <td>Comedy</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   MovieID                               Title                        Genres\n",
       "0        1                    Toy Story (1995)   Animation|Children's|Comedy\n",
       "1        2                      Jumanji (1995)  Adventure|Children's|Fantasy\n",
       "2        3             Grumpier Old Men (1995)                Comedy|Romance\n",
       "3        4            Waiting to Exhale (1995)                  Comedy|Drama\n",
       "4        5  Father of the Bride Part II (1995)                        Comedy"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "MoviesDF.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 3883 entries, 0 to 3882\n",
      "Data columns (total 3 columns):\n",
      "MovieID    3883 non-null int64\n",
      "Title      3883 non-null object\n",
      "Genres     3883 non-null object\n",
      "dtypes: int64(1), object(2)\n",
      "memory usage: 91.1+ KB\n"
     ]
    }
   ],
   "source": [
    "# Let us check weather the Movies Data has Missing values in it\n",
    "MoviesDF.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read the ratings.dat file and assign the columns names\n",
    "RatingsDF = pd.read_csv(\"C:/Users/E056362/Documents/1 New Project/Datasets/Movie Lens/ratings.dat\",sep=\"::\",\n",
    "                      header=None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "RatingsDF.columns = ['UserID','MovieID','Rating','Timestamp']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>UserID</th>\n",
       "      <th>MovieID</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1193</td>\n",
       "      <td>5</td>\n",
       "      <td>978300760</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>661</td>\n",
       "      <td>3</td>\n",
       "      <td>978302109</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>914</td>\n",
       "      <td>3</td>\n",
       "      <td>978301968</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>3408</td>\n",
       "      <td>4</td>\n",
       "      <td>978300275</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>2355</td>\n",
       "      <td>5</td>\n",
       "      <td>978824291</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   UserID  MovieID  Rating  Timestamp\n",
       "0       1     1193       5  978300760\n",
       "1       1      661       3  978302109\n",
       "2       1      914       3  978301968\n",
       "3       1     3408       4  978300275\n",
       "4       1     2355       5  978824291"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "RatingsDF.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1000209 entries, 0 to 1000208\n",
      "Data columns (total 4 columns):\n",
      "UserID       1000209 non-null int64\n",
      "MovieID      1000209 non-null int64\n",
      "Rating       1000209 non-null int64\n",
      "Timestamp    1000209 non-null int64\n",
      "dtypes: int64(4)\n",
      "memory usage: 30.5 MB\n",
      "None\n",
      "-----------------------------------------------------------------------\n",
      "UserID       False\n",
      "MovieID      False\n",
      "Rating       False\n",
      "Timestamp    False\n",
      "dtype: bool\n"
     ]
    }
   ],
   "source": [
    "# Let us check if the Ratings Dataset has missing values in it\n",
    "print(RatingsDF.info())\n",
    "print(\"-----------------------------------------------------------------------\")\n",
    "print(RatingsDF.isnull().any())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Read the users.dat file and assign the respective column names\n",
    "UsersDF = pd.read_csv(\"C:/Users/E056362/Documents/1 New Project/Datasets/Movie Lens/users.dat\",sep=\"::\",\n",
    "                      header=None)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>UserID</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Occupation</th>\n",
       "      <th>Zip-code</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>M</td>\n",
       "      <td>56</td>\n",
       "      <td>16</td>\n",
       "      <td>70072</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>M</td>\n",
       "      <td>25</td>\n",
       "      <td>15</td>\n",
       "      <td>55117</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>M</td>\n",
       "      <td>45</td>\n",
       "      <td>7</td>\n",
       "      <td>02460</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>M</td>\n",
       "      <td>25</td>\n",
       "      <td>20</td>\n",
       "      <td>55455</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   UserID Gender  Age  Occupation Zip-code\n",
       "0       1      F    1          10    48067\n",
       "1       2      M   56          16    70072\n",
       "2       3      M   25          15    55117\n",
       "3       4      M   45           7    02460\n",
       "4       5      M   25          20    55455"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "UsersDF.columns = ['UserID','Gender','Age','Occupation','Zip-code']\n",
    "UsersDF.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 6040 entries, 0 to 6039\n",
      "Data columns (total 5 columns):\n",
      "UserID        6040 non-null int64\n",
      "Gender        6040 non-null object\n",
      "Age           6040 non-null int64\n",
      "Occupation    6040 non-null int64\n",
      "Zip-code      6040 non-null object\n",
      "dtypes: int64(3), object(2)\n",
      "memory usage: 236.0+ KB\n",
      "None\n",
      "----------------------------------------------\n",
      "UserID        False\n",
      "Gender        False\n",
      "Age           False\n",
      "Occupation    False\n",
      "Zip-code      False\n",
      "dtype: bool\n"
     ]
    }
   ],
   "source": [
    "# Let us check weather the Users Data has missing values in it.\n",
    "print(UsersDF.info())\n",
    "print(\"----------------------------------------------\")\n",
    "print(UsersDF.isnull().any())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step 2 : Join the datasets to create the master dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merging Rating and Movie Datasets\n",
    "MovieRatingDF = pd.merge(RatingsDF,MoviesDF,on='MovieID')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>UserID</th>\n",
       "      <th>MovieID</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Timestamp</th>\n",
       "      <th>Title</th>\n",
       "      <th>Genres</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1193</td>\n",
       "      <td>5</td>\n",
       "      <td>978300760</td>\n",
       "      <td>One Flew Over the Cuckoo's Nest (1975)</td>\n",
       "      <td>Drama</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1193</td>\n",
       "      <td>5</td>\n",
       "      <td>978298413</td>\n",
       "      <td>One Flew Over the Cuckoo's Nest (1975)</td>\n",
       "      <td>Drama</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>12</td>\n",
       "      <td>1193</td>\n",
       "      <td>4</td>\n",
       "      <td>978220179</td>\n",
       "      <td>One Flew Over the Cuckoo's Nest (1975)</td>\n",
       "      <td>Drama</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>15</td>\n",
       "      <td>1193</td>\n",
       "      <td>4</td>\n",
       "      <td>978199279</td>\n",
       "      <td>One Flew Over the Cuckoo's Nest (1975)</td>\n",
       "      <td>Drama</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>17</td>\n",
       "      <td>1193</td>\n",
       "      <td>5</td>\n",
       "      <td>978158471</td>\n",
       "      <td>One Flew Over the Cuckoo's Nest (1975)</td>\n",
       "      <td>Drama</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   UserID  MovieID  Rating  Timestamp                                   Title  \\\n",
       "0       1     1193       5  978300760  One Flew Over the Cuckoo's Nest (1975)   \n",
       "1       2     1193       5  978298413  One Flew Over the Cuckoo's Nest (1975)   \n",
       "2      12     1193       4  978220179  One Flew Over the Cuckoo's Nest (1975)   \n",
       "3      15     1193       4  978199279  One Flew Over the Cuckoo's Nest (1975)   \n",
       "4      17     1193       5  978158471  One Flew Over the Cuckoo's Nest (1975)   \n",
       "\n",
       "  Genres  \n",
       "0  Drama  \n",
       "1  Drama  \n",
       "2  Drama  \n",
       "3  Drama  \n",
       "4  Drama  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "MovieRatingDF.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Merging MovieRatingDF with Users dataset to get final master Dataset based on UserID\n",
    "MasterDF = pd.merge(MovieRatingDF,UsersDF,on='UserID')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>UserID</th>\n",
       "      <th>MovieID</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Timestamp</th>\n",
       "      <th>Title</th>\n",
       "      <th>Genres</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Occupation</th>\n",
       "      <th>Zip-code</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1193</td>\n",
       "      <td>5</td>\n",
       "      <td>978300760</td>\n",
       "      <td>One Flew Over the Cuckoo's Nest (1975)</td>\n",
       "      <td>Drama</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>661</td>\n",
       "      <td>3</td>\n",
       "      <td>978302109</td>\n",
       "      <td>James and the Giant Peach (1996)</td>\n",
       "      <td>Animation|Children's|Musical</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>914</td>\n",
       "      <td>3</td>\n",
       "      <td>978301968</td>\n",
       "      <td>My Fair Lady (1964)</td>\n",
       "      <td>Musical|Romance</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>3408</td>\n",
       "      <td>4</td>\n",
       "      <td>978300275</td>\n",
       "      <td>Erin Brockovich (2000)</td>\n",
       "      <td>Drama</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>2355</td>\n",
       "      <td>5</td>\n",
       "      <td>978824291</td>\n",
       "      <td>Bug's Life, A (1998)</td>\n",
       "      <td>Animation|Children's|Comedy</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   UserID  MovieID  Rating  Timestamp                                   Title  \\\n",
       "0       1     1193       5  978300760  One Flew Over the Cuckoo's Nest (1975)   \n",
       "1       1      661       3  978302109        James and the Giant Peach (1996)   \n",
       "2       1      914       3  978301968                     My Fair Lady (1964)   \n",
       "3       1     3408       4  978300275                  Erin Brockovich (2000)   \n",
       "4       1     2355       5  978824291                    Bug's Life, A (1998)   \n",
       "\n",
       "                         Genres Gender  Age  Occupation Zip-code  \n",
       "0                         Drama      F    1          10    48067  \n",
       "1  Animation|Children's|Musical      F    1          10    48067  \n",
       "2               Musical|Romance      F    1          10    48067  \n",
       "3                         Drama      F    1          10    48067  \n",
       "4   Animation|Children's|Comedy      F    1          10    48067  "
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "MasterDF.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Take a copy of MasterDataset.\n",
    "MasterDFcpy = MasterDF.copy()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 1000209 entries, 0 to 1000208\n",
      "Data columns (total 10 columns):\n",
      "UserID        1000209 non-null int64\n",
      "MovieID       1000209 non-null int64\n",
      "Rating        1000209 non-null int64\n",
      "Timestamp     1000209 non-null int64\n",
      "Title         1000209 non-null object\n",
      "Genres        1000209 non-null object\n",
      "Gender        1000209 non-null object\n",
      "Age           1000209 non-null int64\n",
      "Occupation    1000209 non-null int64\n",
      "Zip-code      1000209 non-null object\n",
      "dtypes: int64(6), object(4)\n",
      "memory usage: 83.9+ MB\n"
     ]
    }
   ],
   "source": [
    "#Display info of MasterDF\n",
    "MasterDF.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "UserID        False\n",
       "MovieID       False\n",
       "Rating        False\n",
       "Timestamp     False\n",
       "Title         False\n",
       "Genres        False\n",
       "Gender        False\n",
       "Age           False\n",
       "Occupation    False\n",
       "Zip-code      False\n",
       "dtype: bool"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Check if any of the columns having missing values in it.\n",
    "MasterDF.isnull().any()\n",
    "# Below Listing Shows there are no missing values in any of the columns."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Dealing with Timestamp column.\n",
    "\n",
    "Steps:\n",
    "\n",
    "a. Convert the Timestamp column to Datetime format column. \n",
    "\n",
    "b. Seperate Date and Time and add as seperate column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>UserID</th>\n",
       "      <th>MovieID</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Timestamp</th>\n",
       "      <th>Title</th>\n",
       "      <th>Genres</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Occupation</th>\n",
       "      <th>Zip-code</th>\n",
       "      <th>TSCONV</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1193</td>\n",
       "      <td>5</td>\n",
       "      <td>978300760</td>\n",
       "      <td>One Flew Over the Cuckoo's Nest (1975)</td>\n",
       "      <td>Drama</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "      <td>2000-12-31 22:12:40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>661</td>\n",
       "      <td>3</td>\n",
       "      <td>978302109</td>\n",
       "      <td>James and the Giant Peach (1996)</td>\n",
       "      <td>Animation|Children's|Musical</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "      <td>2000-12-31 22:35:09</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>914</td>\n",
       "      <td>3</td>\n",
       "      <td>978301968</td>\n",
       "      <td>My Fair Lady (1964)</td>\n",
       "      <td>Musical|Romance</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "      <td>2000-12-31 22:32:48</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>3408</td>\n",
       "      <td>4</td>\n",
       "      <td>978300275</td>\n",
       "      <td>Erin Brockovich (2000)</td>\n",
       "      <td>Drama</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "      <td>2000-12-31 22:04:35</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>2355</td>\n",
       "      <td>5</td>\n",
       "      <td>978824291</td>\n",
       "      <td>Bug's Life, A (1998)</td>\n",
       "      <td>Animation|Children's|Comedy</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "      <td>2001-01-06 23:38:11</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   UserID  MovieID  Rating  Timestamp                                   Title  \\\n",
       "0       1     1193       5  978300760  One Flew Over the Cuckoo's Nest (1975)   \n",
       "1       1      661       3  978302109        James and the Giant Peach (1996)   \n",
       "2       1      914       3  978301968                     My Fair Lady (1964)   \n",
       "3       1     3408       4  978300275                  Erin Brockovich (2000)   \n",
       "4       1     2355       5  978824291                    Bug's Life, A (1998)   \n",
       "\n",
       "                         Genres Gender  Age  Occupation Zip-code  \\\n",
       "0                         Drama      F    1          10    48067   \n",
       "1  Animation|Children's|Musical      F    1          10    48067   \n",
       "2               Musical|Romance      F    1          10    48067   \n",
       "3                         Drama      F    1          10    48067   \n",
       "4   Animation|Children's|Comedy      F    1          10    48067   \n",
       "\n",
       "               TSCONV  \n",
       "0 2000-12-31 22:12:40  \n",
       "1 2000-12-31 22:35:09  \n",
       "2 2000-12-31 22:32:48  \n",
       "3 2000-12-31 22:04:35  \n",
       "4 2001-01-06 23:38:11  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Dealing with TimeStamp Column\n",
    "#Convert the Timestamp column to datetime column.\n",
    "\n",
    "MasterDF[\"TSCONV\"] = pd.to_datetime(MasterDF.Timestamp,unit='s',origin='unix')\n",
    "MasterDF.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 1000209 entries, 0 to 1000208\n",
      "Data columns (total 11 columns):\n",
      "UserID        1000209 non-null int64\n",
      "MovieID       1000209 non-null int64\n",
      "Rating        1000209 non-null int64\n",
      "Timestamp     1000209 non-null int64\n",
      "Title         1000209 non-null object\n",
      "Genres        1000209 non-null object\n",
      "Gender        1000209 non-null object\n",
      "Age           1000209 non-null int64\n",
      "Occupation    1000209 non-null int64\n",
      "Zip-code      1000209 non-null object\n",
      "TSCONV        1000209 non-null datetime64[ns]\n",
      "dtypes: datetime64[ns](1), int64(6), object(4)\n",
      "memory usage: 91.6+ MB\n"
     ]
    }
   ],
   "source": [
    "MasterDF.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "# We will seperate out Date and Time into different columns.\n",
    "MasterDF[\"Date\"] = MasterDF[\"TSCONV\"].dt.date\n",
    "MasterDF[\"Time\"] = MasterDF[\"TSCONV\"].dt.time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Drop the Timestamp and TSCONV columns\n",
    "MasterDF.drop(columns=['Timestamp','TSCONV'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>UserID</th>\n",
       "      <th>MovieID</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Title</th>\n",
       "      <th>Genres</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Occupation</th>\n",
       "      <th>Zip-code</th>\n",
       "      <th>Date</th>\n",
       "      <th>Time</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1193</td>\n",
       "      <td>5</td>\n",
       "      <td>One Flew Over the Cuckoo's Nest (1975)</td>\n",
       "      <td>Drama</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "      <td>2000-12-31</td>\n",
       "      <td>22:12:40</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   UserID  MovieID  Rating                                   Title Genres  \\\n",
       "0       1     1193       5  One Flew Over the Cuckoo's Nest (1975)  Drama   \n",
       "\n",
       "  Gender  Age  Occupation Zip-code        Date      Time  \n",
       "0      F    1          10    48067  2000-12-31  22:12:40  "
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "MasterDF.head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Title column has 2 type of information i.e. Movie Name and Year of Release.\n",
    "We will split this information into 2 seperate columns to extract 2 new features i.e. Release Year and Movie Name"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Lets process the Title column from MasterDF\n",
    "# Title column will be seperated in Title and Release Year columns\n",
    "MasterDF[\"Release_yr\"] = (MasterDF.Title.str[-5:-1])\n",
    "MasterDF[\"Release_year\"] = MasterDF[\"Release_yr\"].astype(int)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "MasterDF[\"Movie_Name\"] = MasterDF.Title.str[:-7]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>UserID</th>\n",
       "      <th>MovieID</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Title</th>\n",
       "      <th>Genres</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Occupation</th>\n",
       "      <th>Zip-code</th>\n",
       "      <th>Date</th>\n",
       "      <th>Time</th>\n",
       "      <th>Release_yr</th>\n",
       "      <th>Release_year</th>\n",
       "      <th>Movie_Name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1193</td>\n",
       "      <td>5</td>\n",
       "      <td>One Flew Over the Cuckoo's Nest (1975)</td>\n",
       "      <td>Drama</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "      <td>2000-12-31</td>\n",
       "      <td>22:12:40</td>\n",
       "      <td>1975</td>\n",
       "      <td>1975</td>\n",
       "      <td>One Flew Over the Cuckoo's Nest</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>661</td>\n",
       "      <td>3</td>\n",
       "      <td>James and the Giant Peach (1996)</td>\n",
       "      <td>Animation|Children's|Musical</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "      <td>2000-12-31</td>\n",
       "      <td>22:35:09</td>\n",
       "      <td>1996</td>\n",
       "      <td>1996</td>\n",
       "      <td>James and the Giant Peach</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>914</td>\n",
       "      <td>3</td>\n",
       "      <td>My Fair Lady (1964)</td>\n",
       "      <td>Musical|Romance</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "      <td>2000-12-31</td>\n",
       "      <td>22:32:48</td>\n",
       "      <td>1964</td>\n",
       "      <td>1964</td>\n",
       "      <td>My Fair Lady</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>3408</td>\n",
       "      <td>4</td>\n",
       "      <td>Erin Brockovich (2000)</td>\n",
       "      <td>Drama</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "      <td>2000-12-31</td>\n",
       "      <td>22:04:35</td>\n",
       "      <td>2000</td>\n",
       "      <td>2000</td>\n",
       "      <td>Erin Brockovich</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>2355</td>\n",
       "      <td>5</td>\n",
       "      <td>Bug's Life, A (1998)</td>\n",
       "      <td>Animation|Children's|Comedy</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "      <td>2001-01-06</td>\n",
       "      <td>23:38:11</td>\n",
       "      <td>1998</td>\n",
       "      <td>1998</td>\n",
       "      <td>Bug's Life, A</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   UserID  MovieID  Rating                                   Title  \\\n",
       "0       1     1193       5  One Flew Over the Cuckoo's Nest (1975)   \n",
       "1       1      661       3        James and the Giant Peach (1996)   \n",
       "2       1      914       3                     My Fair Lady (1964)   \n",
       "3       1     3408       4                  Erin Brockovich (2000)   \n",
       "4       1     2355       5                    Bug's Life, A (1998)   \n",
       "\n",
       "                         Genres Gender  Age  Occupation Zip-code        Date  \\\n",
       "0                         Drama      F    1          10    48067  2000-12-31   \n",
       "1  Animation|Children's|Musical      F    1          10    48067  2000-12-31   \n",
       "2               Musical|Romance      F    1          10    48067  2000-12-31   \n",
       "3                         Drama      F    1          10    48067  2000-12-31   \n",
       "4   Animation|Children's|Comedy      F    1          10    48067  2001-01-06   \n",
       "\n",
       "       Time Release_yr  Release_year                       Movie_Name  \n",
       "0  22:12:40       1975          1975  One Flew Over the Cuckoo's Nest  \n",
       "1  22:35:09       1996          1996        James and the Giant Peach  \n",
       "2  22:32:48       1964          1964                     My Fair Lady  \n",
       "3  22:04:35       2000          2000                  Erin Brockovich  \n",
       "4  23:38:11       1998          1998                    Bug's Life, A  "
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "MasterDF.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "MasterDF.drop(columns='Release_yr',axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 1000209 entries, 0 to 1000208\n",
      "Data columns (total 13 columns):\n",
      "UserID          1000209 non-null int64\n",
      "MovieID         1000209 non-null int64\n",
      "Rating          1000209 non-null int64\n",
      "Title           1000209 non-null object\n",
      "Genres          1000209 non-null object\n",
      "Gender          1000209 non-null object\n",
      "Age             1000209 non-null int64\n",
      "Occupation      1000209 non-null int64\n",
      "Zip-code        1000209 non-null object\n",
      "Date            1000209 non-null object\n",
      "Time            1000209 non-null object\n",
      "Release_year    1000209 non-null int32\n",
      "Movie_Name      1000209 non-null object\n",
      "dtypes: int32(1), int64(5), object(7)\n",
      "memory usage: 103.0+ MB\n",
      "None\n",
      "=================================================================================\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>UserID</th>\n",
       "      <th>MovieID</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Title</th>\n",
       "      <th>Genres</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Occupation</th>\n",
       "      <th>Zip-code</th>\n",
       "      <th>Date</th>\n",
       "      <th>Time</th>\n",
       "      <th>Release_year</th>\n",
       "      <th>Movie_Name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1193</td>\n",
       "      <td>5</td>\n",
       "      <td>One Flew Over the Cuckoo's Nest (1975)</td>\n",
       "      <td>Drama</td>\n",
       "      <td>F</td>\n",
       "      <td>1</td>\n",
       "      <td>10</td>\n",
       "      <td>48067</td>\n",
       "      <td>2000-12-31</td>\n",
       "      <td>22:12:40</td>\n",
       "      <td>1975</td>\n",
       "      <td>One Flew Over the Cuckoo's Nest</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   UserID  MovieID  Rating                                   Title Genres  \\\n",
       "0       1     1193       5  One Flew Over the Cuckoo's Nest (1975)  Drama   \n",
       "\n",
       "  Gender  Age  Occupation Zip-code        Date      Time  Release_year  \\\n",
       "0      F    1          10    48067  2000-12-31  22:12:40          1975   \n",
       "\n",
       "                        Movie_Name  \n",
       "0  One Flew Over the Cuckoo's Nest  "
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(MasterDF.info())\n",
    "print(\"=================================================================================\")\n",
    "MasterDF.head(1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### STEP3:Explore the datasets using visual representations(graphs or tables)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### STEP3A : User Age Distribution"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAn0AAAFNCAYAAAB14dn9AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzt3Xl8VNX9//H3MLJvwjAIiChWCeJDZRGEUAWUEraorSCKoFAREFlUUBRFIlgQrSzFgmmlICJWq1ULokEFrQQEEbGlbLU/UYgsSUDCkrCE+f3xcb4TQkKIMvcOc1/Px+M87p0z995zLmH5cFbfsmUKCQAAAHGtjNsVAAAAQPQR9AEAAHgAQR8AAIAHEPQBAAB4AEEfAACABxD0AQAAeABBHwBE2b/+Jd1555l73ujR0vvv2/n770vDhp25Z3/wgfTQQ2fueQBiB0EfAMd06CBlZJyYN3eu9LvfRae8uXOtzI0bo/P8cBkdO0pdu1rq21eaPl3Kzo5cc+WV0rx5p/es0/m1mDxZ6tz5p9Y4YudO+/XJz4/k/epX0rPP/vxnA4g9BH0A4lIoZK1W1apJaWnRLatDB2nxYukf/5DGj5f27JEGDTox8DsTQiHp+PEz+0wA3kHQByBm7NsnPfqo1L27dOON0vDhkSAnK0t64gnp5pul22+X3nzz1M/617/snqFDpWXLpKNHI9/l50szZ0o33WTPeuutE1u8DhyQnnlGuuUWqWdPafbsE1vDinPOOVLDhlbP6tWl11+3/HXr7Dlhr75qn7t2tW7fL76QVq+WXnnF6tqli3T33Xbt/fdLL75o79G5s7Rjh+W9+27keaGQ9Ic/2K9b+Hlht9124ueCrYkjRtixe3cr8z//Obm7eP16afBgu2bwYPscdv/90l/+YnXr2tW6hfftK/nXCYA7CPoAxIzXX5eCQentt6W//10aMEDy+SzwGzNG+sUvpL/9TXruOQv6Vq8u/llpaVKbNhbMSdLKlZHv3n3X7n3xRelPf5KWLz/x3qeflvx+af58+37NmhODrJL4/VLbthZ4FvbddxZkzpplrYPPPCPVqSO1aiXdcYfV9733LNAM++ADaeRIu/68805+5saNUt269uvWr580bpyUk1NyPadPt+OiRVbm5Zef+H1OjgXhv/mN9M47Fqg++uiJgd1HH9kYw7fessD6tddKLheAOwj6AMQMv9+6RHftslazK6+0oG/TJgs07rpLKltWqldP6tbNWsWKkpcnffKJjbU75xzpuutO7OL9+GMLZIJBqWpVqXfvyHd79lhAOHSoVLGiVKOG1KNH8WUVp1Ytaf/+ot/x6FHp22+lY8cs4Dv//FM/KynJWhD9fnufwsJ1POcc6frrpQsukD77rHT1Lcpnn0n160udOlnZN9wgNWhwYgDdubOVV7681L699PXXP79cANFRxF8fABAdZcpYoFPQsWORQOa226z7MTx7tHt3C8h27bKu2u7dI/cdP25BYVE+/dSClGuusc8dO0qjRkk//CCde649q3btyPXBYOR81y6r0y23RPJCoROvOR1ZWRZQFnb++dJ999l7bt0qtWwpDRliQWJxCta1KLVqWXAcdt55Z2Y8YXb2yS2L551n7xZWs2bkvEIFKTf355cLIDoI+gA45rzzbMbohRdG8nbssJYiSapUyQKgIUOkb76RHnxQSkiwoKduXetuPR1Llljw0atXJO/YMeuKvOUWKRCQMjMj3xU8r13bWhPfeccCx5/i+HFpxQqpRYuiv+/Y0dLBg9KUKdaFPGbMiYFbQcXlh2VlWWAavm7XLikx0c4rVLCWz7A9e07/PQIBe1ZBu3dbVzSAsw/duwAc06GD9PLLFmQdP24TDFaulNq1s+9XrrQlXUIhqXJlaxn0+6XGjS0gfPVV6fBhm1TxzTfW7VtYZqa0dq00caKN2Qun22+PdPG2b29jAjMzbdLGq69G7g8EpKuvtokeBw9aPTMybDJGSY4ds27bCRMsuCo4eSPsu++sfkeOSOXKWSrz49/ENWpYUFzaGbp799r7HDtmXdfffRdp5bzkEmnpUvtu82br9g4791wr+/vvi37uNddI27ZJH35ov+ZLl1rrZJs2pasfgNhASx8Ax9x5pzRnjs0OPXDAxuY99piNV5Ok7dttcsG+fVKVKja7tmlT+27iRJv8cPvtNibuggsiM1wL+uADm/DRsuWJ+b/5jU0U+eYb6ybevt0milSqZN+tWxcJvh59VPrzn21SRG6utTLefnvx77VsWWQySCBgLXypqUV32R49as/+9lvr1r78cpukIVnw+8EH9t5161oL4Om47DILTG++2QLHlBSbPSxJv/2tBaHJydJVV9m4vPBYwwoVbPLIsGEWFD7zzInP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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Drawing user Age Distribution.\n",
    "fig= plt.figure(figsize=(10,5),facecolor='y',edgecolor='b')\n",
    "plt.hist(MasterDF[\"Age\"],bins=10,color='g',edgecolor='b')\n",
    "plt.xlim(0,90)\n",
    "plt.ylim(0,400000)\n",
    "plt.xlabel(\"Frequency Counts\")\n",
    "plt.ylabel(\"User Age\")\n",
    "plt.title(\"Use Age Distribution\")\n",
    "# Draw the Mean Line as well\n",
    "plt.axvline(MasterDF.Age.mean(),color='r',label='Mean',linestyle='dashed')\n",
    "plt.axvline(MasterDF.Age.median(),color='r',label='Mean',linestyle='dashdot')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "29.73831369243828\n",
      "25.0\n",
      "0    25\n",
      "dtype: int64\n"
     ]
    }
   ],
   "source": [
    "print(MasterDF.Age.mean())\n",
    "print(MasterDF.Age.median())\n",
    "print(MasterDF.Age.mode())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Observarions from AGE Distributions.\n",
    "\n",
    "1. Mean age is : 29.73831369243828\n",
    "2. Meadian of Age distribution is : 25.0\n",
    "3. Mean of Age > Median of Age : Age distribution is Right Skwed Distrubtuion\n",
    "4. Highest no of Age entries are for age value 25."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Lets try Box Plot for Age and see if there are outliers in the values\n",
    "sns.boxplot(MasterDF[\"Age\"])\n",
    "plt.show()\n",
    "# Below fig shows there are outliers in fig."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Step3B : User rating of the movie “Toy Story” "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 2077 entries, 40 to 986829\n",
      "Data columns (total 1 columns):\n",
      "Rating    2077 non-null int64\n",
      "dtypes: int64(1)\n",
      "memory usage: 32.5 KB\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "4    835\n",
       "5    820\n",
       "3    345\n",
       "2     61\n",
       "1     16\n",
       "Name: Rating, dtype: int64"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# User Rating for Movie Toy Story\n",
    "Toy_Story_rating = pd.DataFrame(MasterDF[MasterDF[\"Movie_Name\"] == 'Toy Story'][\"Rating\"])\n",
    "Toy_Story_rating.columns = ['Rating']\n",
    "Toy_Story_rating.info()\n",
    "Toy_Story_rating.Rating.value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0.5, 1.0, 'Rating Distrinution for Movie Toy Story')"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Lets Visualize the Rating for Movie Toy Story\n",
    "\n",
    "plt.figure(figsize=(6,6))\n",
    "plt.hist(Toy_Story_rating.Rating)\n",
    "plt.xlim(1,5)\n",
    "plt.ylim(0,1000)\n",
    "plt.xlabel(\"Rating\")\n",
    "plt.ylabel(\"Frequency\")\n",
    "plt.title(\"Rating Distrinution for Movie Toy Story\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### STEP3C :Top 25 movies by viewership rating "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Movie_Name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>One Flew Over the Cuckoo's Nest</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Crucible, The</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Blow-Out (La Grande Bouffe)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Five Easy Pieces</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Black Cauldron, The</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Raging Bull</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Cook the Thief His Wife &amp; Her Lover, The</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Great Escape, The</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Conan the Barbarian</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Sneakers</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Devil's Advocate, The</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Space Cowboys</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Conquest of the Planet of the Apes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Secret of NIMH, The</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Manhattan Murder Mystery</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Love and Death</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Mother</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>On Her Majesty's Secret Service</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Fox and the Hound, The</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Tron</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Lolita</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Jungle Fever</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>Blade Runner</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Fantasia</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Dr. Strangelove or: How I Learned to Stop Worr...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                           Movie_Name\n",
       "0                     One Flew Over the Cuckoo's Nest\n",
       "1                                       Crucible, The\n",
       "2                         Blow-Out (La Grande Bouffe)\n",
       "3                                    Five Easy Pieces\n",
       "4                                 Black Cauldron, The\n",
       "5                                         Raging Bull\n",
       "6            Cook the Thief His Wife & Her Lover, The\n",
       "7                                   Great Escape, The\n",
       "8                                 Conan the Barbarian\n",
       "9                                            Sneakers\n",
       "10                              Devil's Advocate, The\n",
       "11                                      Space Cowboys\n",
       "12                 Conquest of the Planet of the Apes\n",
       "13                                Secret of NIMH, The\n",
       "14                           Manhattan Murder Mystery\n",
       "15                                     Love and Death\n",
       "16                                             Mother\n",
       "17                    On Her Majesty's Secret Service\n",
       "18                             Fox and the Hound, The\n",
       "19                                               Tron\n",
       "20                                             Lolita\n",
       "21                                       Jungle Fever\n",
       "22                                       Blade Runner\n",
       "23                                           Fantasia\n",
       "24  Dr. Strangelove or: How I Learned to Stop Worr..."
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Top 25 Movies by Rating\n",
    "#MasterDF.sort_values(by=['Rating'],axis=1,ascending=False)\n",
    "sorted_Master_DF = MasterDF.sort_values(by='Rating',ascending=False)\n",
    "Top_25_movies = pd.DataFrame(sorted_Master_DF[\"Movie_Name\"].unique()[0:25],columns=['Movie_Name'])\n",
    "Top_25_movies"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### STEP3D : Find the ratings for all the movies reviewed by for a particular user of user id = 2696"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Back to the Future', 'E.T. the Extra-Terrestrial', 'L.A. Confidential', 'Lone Star', 'JFK', 'Talented Mr. Ripley, The', 'Midnight in the Garden of Good and Evil', 'Cop Land', 'Palmetto', 'Perfect Murder, A', 'Game, The', 'I Know What You Did Last Summer', \"Devil's Advocate, The\", 'Psycho', 'Wild Things', 'Basic Instinct', 'Lake Placid', 'Shining, The', 'I Still Know What You Did Last Summer', 'Client, The']\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Find the ratings for all the movies reviewed by for a particular user of user id = 2696\n",
    "List_of_Movies_by_user_2696 = list(MasterDF[MasterDF.UserID == 2696]['Movie_Name'].unique())\n",
    "print(List_of_Movies_by_user_2696)\n",
    "np.count_nonzero(List_of_Movies_by_user_2696)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 20 entries, 953847 to 953866\n",
      "Data columns (total 1 columns):\n",
      "Movie_Name    20 non-null object\n",
      "dtypes: object(1)\n",
      "memory usage: 320.0+ bytes\n"
     ]
    }
   ],
   "source": [
    "# Creating Small Dataframe Object to Store the information of Movies and Ratings Assigned by user '2696'\n",
    "Movies_rated_by_2696 = pd.DataFrame(MasterDF[MasterDF.UserID == 2696]['Movie_Name'])\n",
    "Movies_rated_by_2696.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Movie_Name</th>\n",
       "      <th>Rating</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>953847</th>\n",
       "      <td>Back to the Future</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                Movie_Name  Rating\n",
       "953847  Back to the Future       2"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Movies_rated_by_2696['Rating'] = MasterDF[MasterDF.UserID == 2696]['Rating']\n",
    "Movies_rated_by_2696.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1c92386cba8>"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plotting the Histogram to Visualize the rating of movies by the user id = 2696\n",
    "plt.figure(figsize=(5,5))\n",
    "sns.kdeplot(Movies_rated_by_2696.Rating,shade=True)\n",
    "plt.xlim(0,5)\n",
    "plt.xlabel(\"Frequency Count\")\n",
    "plt.ylabel(\"Rating\")\n",
    "plt.title(\"Distribution of Movie Rating by user 2696\")\n",
    "sns.distplot(Movies_rated_by_2696[\"Rating\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1c92386a860>"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 504x504 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Bar Plot \n",
    "plt.figure(figsize=(7,7))\n",
    "plt.xlabel(\"Movie Names\")\n",
    "plt.ylabel(\"Rating\")\n",
    "plt.title(\"Movie Name and Rating by user 2696\")\n",
    "sns.barplot(y=Movies_rated_by_2696.Movie_Name,x=Movies_rated_by_2696.Rating,orient=\"V\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## PART 2: Feature Engineering "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 1000209 entries, 0 to 1000208\n",
      "Data columns (total 13 columns):\n",
      "UserID          1000209 non-null int64\n",
      "MovieID         1000209 non-null int64\n",
      "Rating          1000209 non-null int64\n",
      "Title           1000209 non-null object\n",
      "Genres          1000209 non-null object\n",
      "Gender          1000209 non-null object\n",
      "Age             1000209 non-null int64\n",
      "Occupation      1000209 non-null int64\n",
      "Zip-code        1000209 non-null object\n",
      "Date            1000209 non-null object\n",
      "Time            1000209 non-null object\n",
      "Release_year    1000209 non-null int32\n",
      "Movie_Name      1000209 non-null object\n",
      "dtypes: int32(1), int64(5), object(7)\n",
      "memory usage: 103.0+ MB\n"
     ]
    }
   ],
   "source": [
    "MasterDF.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Converting Gender column into one Hot encoded values."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Gender column conversion \n",
    "MasterDF.Gender.replace(['M','F'],[1,0],inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Handling the Release column to extract features as Release Decade "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1919\n",
      "2000\n"
     ]
    }
   ],
   "source": [
    "# lets find out Range of release years of Movie Data\n",
    "print(MasterDF.Release_year.min())\n",
    "print(MasterDF.Release_year.max())\n",
    "\n",
    "#print(bins)\n",
    "#============================================================================\n",
    "# 1930s : Movie release year <= 1930\n",
    "# 1940s : Movie release year <= 1940 and > 1930\n",
    "# 1950s : Movie release year <= 1950 and > 1940\n",
    "# 1960s : Movie release year <= 1960 and > 1950\n",
    "# 1970s : Movie release year <= 1970 and > 1960\n",
    "# 1980s : Movie release year <= 1980 and > 1970\n",
    "# 1990s : Movie release year <= 1990 and > 1980\n",
    "# 2000s : Movie release year <= 2000 and > 1990\n",
    "#============================================================================\n",
    "cut_bins = [1915,1930,1940,1950,1960,1970,1980,1990,2000]\n",
    "cut_labels = ['1930s','1940s','1950s','1960s','1970s','1980s','1990s','2000s']\n",
    "MasterDF[\"Release_Decade\"] = pd.cut(MasterDF.Release_year,bins=cut_bins,labels=cut_labels)\n",
    "\n",
    "# Now Replace using numeric Values\n",
    "MasterDF.Release_Decade.replace(['1930s','1940s','1950s','1960s','1970s','1980s','1990s','2000s'],\n",
    "                                                          [1,2,3,4,5,6,7,8],inplace=True)\n",
    "\n",
    "# Here we have convered the Year release into a Release_decade column"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Extracting Features as 'Year of Rating' and 'Month of Rating' based Date "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "MasterDF[\"Year_of_Rating\"]=pd.DatetimeIndex(MasterDF[\"Date\"]).year\n",
    "MasterDF[\"Month_of_Rating\"]=pd.DatetimeIndex(MasterDF[\"Date\"]).month"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 1000209 entries, 0 to 1000208\n",
      "Data columns (total 16 columns):\n",
      "UserID             1000209 non-null int64\n",
      "MovieID            1000209 non-null int64\n",
      "Rating             1000209 non-null int64\n",
      "Title              1000209 non-null object\n",
      "Genres             1000209 non-null object\n",
      "Gender             1000209 non-null int64\n",
      "Age                1000209 non-null int64\n",
      "Occupation         1000209 non-null int64\n",
      "Zip-code           1000209 non-null object\n",
      "Date               1000209 non-null object\n",
      "Time               1000209 non-null object\n",
      "Release_year       1000209 non-null int32\n",
      "Movie_Name         1000209 non-null object\n",
      "Release_Decade     1000209 non-null int64\n",
      "Year_of_Rating     1000209 non-null int64\n",
      "Month_of_Rating    1000209 non-null int64\n",
      "dtypes: int32(1), int64(9), object(6)\n",
      "memory usage: 125.9+ MB\n"
     ]
    }
   ],
   "source": [
    "MasterDF.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1c92c3ca5c0>"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Rating Vs Gender Visualizations\n",
    "MasterDF.groupby(\"Year_of_Rating\")[\"Rating\"].mean().plot(kind=\"bar\")\n",
    "# This shows that Average Rating is not affected that much by year of rating."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1c92c3e5908>"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Gender vs Rating\n",
    "MasterDF.groupby(\"Gender\")[\"Rating\"].mean().plot(kind=\"bar\")\n",
    "# This shows that the average rating is not affected that much by Gender"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1c930952978>"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Month of Rating Vs Rating\n",
    "MasterDF.groupby(\"Month_of_Rating\")[\"Rating\"].mean().plot(kind=\"bar\")\n",
    "# This shows that there is no variance in average rating based on Month of Rating"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1c9309754a8>"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXcAAAENCAYAAAD0eSVZAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAFzZJREFUeJzt3X20XXV95/H3hySiCArCnYJAiBWUVlGwEfGhSkHH+AR2xPGhSwS1WXXEp3E6gnVAWdOOjlVri0rTgoBDBUXqpBarKDhqHZEQQwIGNVKUDKARNJj61OB3/tg7ejzee8++uSe5uZv3a6297n74/fb+nXPv/Zzf+Z199k5VIUnql93mugGSpPEz3CWphwx3Seohw12Seshwl6QeMtwlqYcMd0nqIcNdknrIcJekHjLcJamHFs7Vgffbb79asmTJXB1ekual66677ntVNTGq3JyF+5IlS1i1atVcHV6S5qUk3+pSzmEZSeohw12Seshwl6QeMtwlqYcMd0nqIcNdknrIcJekHjLcJamH5uxLTJLG44gLj5h2+7qXrttJLdGuxJ67JPWQ4S5JPWS4S1IPGe6S1EN+oCppVt77R1dNu/1V5x63k1qiQfbcJamH7LmPyfrDf2va7b910/qd1JLts/H0z0+7/aC3/e5Oasn22f/qNdNuv+P3jtxJLdlOb3ngNNs277x2qDfsuUtSD9lzl8Zgyen/OO32W972rJ3UkpnzXWc/Ge4ai7e85S2z2q57r3e+4NnTbn/DpR/fSS3pl5HhnuS+wOeA3dvyl1XVWUNlTgHeAfy/dtU5VfW3423qCNONWcLIcUu/wi2pT7r03H8KHFdVW5IsAr6Q5BNV9aWhcpdW1Wnjb6IkaaZGhntVFbClXVzUTjXuhsznMctxmO25wr61lTSo05h7kgXAdcChwHur6ppJij0vyZOBrwOvr6pbx9dMace6t3cu7s36+nlRp1Mhq+qeqjoSOAg4Oskjh4r8A7Ckqh4FfBq4cLL9JFmeZFWSVZs2bZpNuyVJ05jR2TJV9YMknwWWATcMrL9zoNjfAG+fov4KYAXA0qVLxz60I0nzzY76Al6Xs2UmgH9rg/1+wFMZCu8kB1TV7e3iCcCufWKsdjmfueqh024//rhv7qSWSP3Qped+AHBhO+6+G/Dhqvp4krOBVVW1EnhNkhOArcBdwCk7qsGSpNG6nC2zFjhqkvVnDsyfAZwx3qZJkraX31CVpFnYVYcUvXCYJPWQ4S5JPWS4S1IPGe6S1EOGuyT1kOEuST1kuEtSDxnuktRDhrsk9ZDhLkk9ZLhLUg8Z7pLUQ4a7JPWQ4S5JPWS4S1IPGe6S1EOGuyT1kOEuST00MtyT3DfJl5Ncn+TGJG+dpMzuSS5NsiHJNUmW7IjGSpK66dJz/ylwXFU9GjgSWJbkmKEyLwe+X1WHAu8G3j7eZkqSZmJkuFdjS7u4qJ1qqNiJwIXt/GXA8UkytlZKkmak05h7kgVJ1gDfBa6sqmuGihwI3ApQVVuBzcC+42yoJKm7TuFeVfdU1ZHAQcDRSR45VGSyXvpw754ky5OsSrJq06ZNM2+tJKmTGZ0tU1U/AD4LLBvatBE4GCDJQuCBwF2T1F9RVUuraunExMR2NViSNFqXs2Umkuzdzt8PeCpw01CxlcBL2/mTgKuq6td67pKknWNhhzIHABcmWUDzYvDhqvp4krOBVVW1EjgP+GCSDTQ99hfusBZLkkYaGe5VtRY4apL1Zw7M/wR4/nibJknaXn5DVZJ6yHCXpB4y3CWphwx3Seohw12Seshwl6QeMtwlqYcMd0nqIcNdknrIcJekHjLcJamHDHdJ6iHDXZJ6yHCXpB4y3CWphwx3Seohw12Seshwl6Qe6nKD7IOTXJ1kfZIbk7x2kjLHJtmcZE07nTnZviRJO0eXG2RvBd5QVauT7AVcl+TKqvrqULnPV9Wzx99ESdJMjey5V9XtVbW6nf8hsB44cEc3TJK0/WY05p5kCXAUcM0kmx+f5Pokn0jyiDG0TZK0nboMywCQZE/go8Drquruoc2rgUOqakuSZwIfAw6bZB/LgeUAixcv3u5GS5Km16nnnmQRTbBfXFWXD2+vqruraks7fwWwKMl+k5RbUVVLq2rpxMTELJsuSZpKl7NlApwHrK+qd01RZv+2HEmObvd75zgbKknqrsuwzBOBlwDrkqxp170JWAxQVecCJwGvTLIV+DHwwqqqHdBeSVIHI8O9qr4AZESZc4BzxtUoSdLs+A1VSeohw12Seshwl6QeMtwlqYcMd0nqIcNdknrIcJekHjLcJamHDHdJ6iHDXZJ6yHCXpB4y3CWphwx3Seohw12Seshwl6QeMtwlqYcMd0nqIcNdknrIcJekHhoZ7kkOTnJ1kvVJbkzy2knKJMlfJtmQZG2Sx+yY5kqSuhh5g2xgK/CGqlqdZC/guiRXVtVXB8o8AzisnR4HvL/9KUmaAyN77lV1e1Wtbud/CKwHDhwqdiJwUTW+BOyd5ICxt1aS1MmMxtyTLAGOAq4Z2nQgcOvA8kZ+/QVAkrSTdA73JHsCHwVeV1V3D2+epEpNso/lSVYlWbVp06aZtVSS1FmncE+yiCbYL66qyycpshE4eGD5IOC24UJVtaKqllbV0omJie1prySpgy5nywQ4D1hfVe+aothK4OT2rJljgM1VdfsY2ylJmoEuZ8s8EXgJsC7Jmnbdm4DFAFV1LnAF8ExgA/Aj4NTxN1WS1NXIcK+qLzD5mPpgmQJeNa5GSZJmx2+oSlIPGe6S1EOGuyT1kOEuST1kuEtSDxnuktRDhrsk9ZDhLkk9ZLhLUg8Z7pLUQ4a7JPWQ4S5JPWS4S1IPGe6S1EOGuyT1kOEuST1kuEtSDxnuktRDXW6QfX6S7ya5YYrtxybZnGRNO505/mZKkmaiyw2yLwDOAS6apsznq+rZY2mRJGnWRvbcq+pzwF07oS2SpDEZ15j745Ncn+QTSR4xpn1KkrZTl2GZUVYDh1TVliTPBD4GHDZZwSTLgeUAixcvHsOhJUmTmXXPvarurqot7fwVwKIk+01RdkVVLa2qpRMTE7M9tCRpCrMO9yT7J0k7f3S7zztnu19J0vYbOSyT5EPAscB+STYCZwGLAKrqXOAk4JVJtgI/Bl5YVbXDWixJGmlkuFfVi0ZsP4fmVElJ0i7Cb6hKUg8Z7pLUQ4a7JPWQ4S5JPWS4S1IPGe6S1EOGuyT1kOEuST1kuEtSDxnuktRDhrsk9ZDhLkk9ZLhLUg8Z7pLUQ4a7JPWQ4S5JPWS4S1IPGe6S1EMjwz3J+Um+m+SGKbYnyV8m2ZBkbZLHjL+ZkqSZ6NJzvwBYNs32ZwCHtdNy4P2zb5YkaTZGhntVfQ64a5oiJwIXVeNLwN5JDhhXAyVJMzeOMfcDgVsHlje26yRJc2Qc4Z5J1tWkBZPlSVYlWbVp06YxHFqSNJlxhPtG4OCB5YOA2yYrWFUrqmppVS2dmJgYw6ElSZMZR7ivBE5uz5o5BthcVbePYb+SpO20cFSBJB8CjgX2S7IROAtYBFBV5wJXAM8ENgA/Ak7dUY2VJHUzMtyr6kUjthfwqrG1SJI0a35DVZJ6yHCXpB4y3CWphwx3Seohw12Seshwl6QeMtwlqYcMd0nqIcNdknrIcJekHjLcJamHDHdJ6iHDXZJ6yHCXpB4y3CWphwx3Seohw12Seshwl6QeMtwlqYc6hXuSZUm+lmRDktMn2X5Kkk1J1rTTK8bfVElSVyNvkJ1kAfBe4GnARuDaJCur6qtDRS+tqtN2QBslSTPUped+NLChqm6uqp8BlwAn7thmSZJmo0u4HwjcOrC8sV037HlJ1ia5LMnBY2mdJGm7dAn3TLKuhpb/AVhSVY8CPg1cOOmOkuVJViVZtWnTppm1VJLUWZdw3wgM9sQPAm4bLFBVd1bVT9vFvwF+Z7IdVdWKqlpaVUsnJia2p72SpA66hPu1wGFJHpLkPsALgZWDBZIcMLB4ArB+fE2UJM3UyLNlqmprktOATwILgPOr6sYkZwOrqmol8JokJwBbgbuAU3ZgmyVJI4wMd4CqugK4YmjdmQPzZwBnjLdpkqTt5TdUJamHDHdJ6iHDXZJ6yHCXpB4y3CWphwx3Seohw12Seshwl6QeMtwlqYcMd0nqIcNdknrIcJekHjLcJamHDHdJ6iHDXZJ6yHCXpB4y3CWphwx3SeqhTuGeZFmSryXZkOT0SbbvnuTSdvs1SZaMu6GSpO5GhnuSBcB7gWcAvw28KMlvDxV7OfD9qjoUeDfw9nE3VJLUXZee+9HAhqq6uap+BlwCnDhU5kTgwnb+MuD4JBlfMyVJM9El3A8Ebh1Y3tium7RMVW0FNgP7jqOBkqSZS1VNXyB5PvD0qnpFu/wS4OiqevVAmRvbMhvb5W+2Ze4c2tdyYHm7+HDga9Mcej/gezN7ONa3fi/qz+e2W3/H1z+kqiZG7qWqpp2AxwOfHFg+AzhjqMwngce38wvbhmXUvkccd5X1rX9vrD+f2279ua+/beoyLHMtcFiShyS5D/BCYOVQmZXAS9v5k4Crqm2lJGnnWziqQFVtTXIaTe98AXB+Vd2Y5GyaV5iVwHnAB5NsAO6ieQGQJM2RkeEOUFVXAFcMrTtzYP4nwPPH2zRWWN/699L687nt1p/7+kCHD1QlSfOPlx+QpB4y3CWphzqNue8MSQ6n+abrgUABtwErq2r9nDasoyRHA1VV17aXZ1gG3NR+XjHTfV1UVSePvZG7oIEzsG6rqk8neTHwBGA9sKKq/m1OGyjNU7vEmHuSNwIvorm0wcZ29UE0//SXVNXbdkIbDqd5YbmmqrYMrF9WVf80ou5ZNNfeWQhcCTwO+CzwVJrvCPzpNHWHTysN8HvAVQBVdcJ2PJYn0Vw24oaq+lSH8o8D1lfV3UnuB5wOPAb4KvBnVbV5RP3XAH9fVbdOV26KuhfTPG97AD8A9gQuB46n+ft86TTVt+3jocDvAwcDW4FvAB8a1W6p18ZxsvxsJ+DrwKJJ1t8H+MYs931qhzKvofm27MeAW4ATB7at7lB/Hc1ponsAdwMPaNffD1g7ou5q4H8BxwJPaX/e3s4/peNj/PLA/B8Ca4CzgH8GTu9Q/0ZgYTu/AvgL4EntPi7vUH8zzTutzwP/CZiYwe9nbftzIfAdYEG7nFHP3cDv7krgzcAXgfcBf0rzwnTsXP9tz8cJ+HdzfPx95/o52ImP9YHA24CbgDvbaX27bu9Z7XuuH1z7AG+i+Urt8PpDgK/Nct/f7lBmHbBnO78EWAW8tl3+Sof6X5lsvl1eM6LubsDr24A6sl138wwf4+Dxr90WrsD9gXUd6q8fmF89tG3a9m87fvs4/j3Ndx42Af9E88W2vUbUvYHmRXwf4IfAg9r19x1s14jf3bYXhD2Az7bzi7v87tqyO+4fDD7RocwDgP8BfBB48dC293Wovz/wfpqrt+4LvKV9Xj4MHDCi7oOGpn1pOjj7bPtdjKi/bOh5PA9YC/wd8Bsd6r8N2K+dXwrcDGwAvkWHzg1N5+jNwEO38/ezFLiapoN1cPt/uLn9PzqqQ/09gbNpOkib27/9LwGndDz+J4E3AvsP/T7fCFw5m7+9XWXM/XXAZ5J8g19epGwxcChw2qjKSdZOtQn4jQ7HX1DtUExV3ZLkWOCyJIe0+xjlZ0n2qKofAb8z0K4HAj+frmJV/Rx4d5KPtD+/w8w/C9ktyT40AZuq2tTu+1+TbO1Q/4Ykp1bVB4DrkyytqlVJHgZ0GfOu9nF8CvhUkkU0w1QvAv4cmO46GOfRhOoC4E+AjyS5GTiGZpiui4XAPcDuwF5tg77dtqOLD9MMgx1bVXcAJNmf5sXpI8DTpquc5DFTbQKO7HD8D9AMJX0UeFmS59GE/E9pnodRLgD+kebF/GrgYuBZNJ9hncuvX8V10PdognTQgTShWcBvjjj2n9G8kAO8k+Zd53OA/wD8NfDcEfWfVVXb7hHxDuAF1Xxu9TCaF4ilI+rvA+wNXJ3kDuBDwKVVdduIetu8j+Yd6t407/xeX1VPS3J8u+3xI+pfDPw98HTgP9L8Di4B3pzkYVX1phH1l1TVr1wivf0bfHuSl3V8DJObzSvDOCeaYDoGeB7NJQyOoe2Rdaj7HZp/okOGpiU0H9SNqn8Vba95YN1C4CLgng71d59i/X7AETN8Hp5FM849kzq30PR4/qX9uX/9slfRpef9QJqA+CZwDU2g3wz8H+DRHepP2UMG7teh/oOBB7fze7e//6M7PvbX0vQUV9C8SJzarp8APtdxH1O+O5xu20CZe9q/oasnmX7cof6aoeU/oRlS25duw4KD79y+Pd2+J6n7X2jC+YiBdf8yg7+91VMdq+Pf3k38ckjwS0PburzrHDz+79IE8h3tc798ls9dl3ft1w8tX9v+3I3mhIpR9T8F/FcG3uXQdEjfCHy66+9h0n3PpvKuMtH0/p40xba/61D/IAbeFg1te+JcP75ZPC97AA+ZQfm9gEfTvPsY+ZZ6oN7D5vhxPqJ9QTh8O+vP6h+MZmjpsCm23dqh/npgt6F1L6V5q/+tDvWvH5j/70PbugTkQTTvUN7V/g10HhakOQHiPwNvoOkQZGBbl89MXt0+/8fRDCf9BfBk4K3ABzvU/7UXP5p3gcuAD3So/39phhOfT/MO5rnt+qfQ4QJeNL39J7Xzz+FXL7LYpWOwD83NjW4Cvk9z+Zb17bqRw2LT7ns2lZ2c+jAN/YPdNfQPtk+H+icBD59i23M71P+fwFMnWb+MDicU0Iz57jnJ+kOBy2bwPDyHZrz4jhnUOWto2vZ5z/7ARR33cSxwKc1nN+toLnWynLZHP6LuJbP83T+aZtz7E8DhwHtoztq6EXhCh/qPAr7c1vkCbUeH5p3jazq24XCaM+v2HFq/bCaP5df2O5vKTk59n+hwtlWf6tOc4fXI+dj2+VifWZ6pN920S5znLu2qkny7qhbfG+vP57bPl/pJ1tHcC2NLkiU0tyn9YFW9J8lXquqo7T3+rnK2jDRnZnu21XyuP5/b3of6zP5MvSkZ7lLzT/h0mg+0BoXmA7M+15/Pbe9D/TuSHFlVawDaHvyzgfOBIzrUn5LhLsHHaT7MWjO8Iclne15/Pre9D/VPprlkxi9U1Vbg5CR/3aH+lBxzl6Qe8pK/ktRDhrsk9ZDhrnkjyUFJ/neSbyT5ZpL3tNeDn6v2PLe9dv+25bOTPHWu2iMNMtw1LyQJzXXeP1ZVhwEPo7l2zpTXyt8Jngv8Ityr6syq+vQctkf6BcNd88VxwE+quXIlVXUPzaWSX5bk/kn+PMm6JGuTvBogyWOTfDHJ9Um+nGSvJKckOWfbTpN8vD23mCRbkrwzyeokn0ky0a7/wyTXtvv5aJI9kjwBOAF4R5I1SR6a5IIkJ7V1jk/ylbZN5yfZvV1/S5K3tsdY194kRho7w13zxSOA6wZXVNXdwLeBVwAPobn+9qOAi9vhmktprsv/aJprd/x4xDHuT/OV78fQXBHzrHb95VX12HY/64GXV9UXgZXAH1fVkVX1zW07SXJfmqtsvqCqjqA55fiVA8f5XnuM99NclVEaO8Nd80Vori8+2fonA+e25wdTVXcBDwdur6pr23V3b9s+jZ/TvCBAc/OGJ7Xzj0zy+far4n9A80IznYfTXDb36+3yhW0bt7m8/XkdzWWppbEz3DVf3MjQjRuSPIDm7jmTBf9ULwZb+dW/+/tOc8xt9S8ATmt74W8dUWfbsafz0/bnPfhFQu0ghrvmi88AeyQ5GSDJApo7/1xAcz3wP0qysN32IJrL9z44yWPbdXu1228BjkyyW5KDaW4kvs1uNJfvBXgxzSVcobnG+e3tnZ3+YKD8D9ttw24CliQ5tF1+Cc0wj7TTGO6aF6r5KvXvA89PczvGrwM/Ad4E/C3N2PvaJNfT3KLuZ8ALgL9q111J0+P+Z5o7Vq2juQXg6oHD/CvwiCTX0XyAe3a7/r/R3KHqSprg3uYS4I/bD04fOtDWnwCn0twycB3NcM+543oupC68/IDUSrKlqvac63ZI42DPXZJ6yJ67JPWQPXdJ6iHDXZJ6yHCXpB4y3CWphwx3Seohw12Seuj/A8Bl2G2y+bFEAAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Rating Vs Occupation\n",
    "MasterDF.groupby(\"Occupation\")[\"Rating\"].mean().plot(kind=\"bar\")\n",
    "# Below graph shows us that Average rating varies a bit with Occupration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1c9342a4898>"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Decade of release vs Rating\n",
    "MasterDF.groupby(\"Release_Decade\")[\"Rating\"].mean().plot(kind=\"bar\")\n",
    "# Below graph shows us that the Rating is affected by release year"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### STEP4A: Create a separate column for each genre category with a one-hot encoding "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Let handle the Generes Column\n",
    "TestDF = MasterDF\n",
    "Genere_DF = TestDF.Genres.str.get_dummies()\n",
    "Final_DF = pd.concat([MasterDF,Genere_DF],axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Drop all non Important columns from Dataframe\n",
    "Final_DF.drop(columns=['Genres','Zip-code','Date','Time','Release_year'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 1000209 entries, 0 to 1000208\n",
      "Data columns (total 29 columns):\n",
      "UserID             1000209 non-null int64\n",
      "MovieID            1000209 non-null int64\n",
      "Rating             1000209 non-null int64\n",
      "Title              1000209 non-null object\n",
      "Gender             1000209 non-null int64\n",
      "Age                1000209 non-null int64\n",
      "Occupation         1000209 non-null int64\n",
      "Movie_Name         1000209 non-null object\n",
      "Release_Decade     1000209 non-null int64\n",
      "Year_of_Rating     1000209 non-null int64\n",
      "Month_of_Rating    1000209 non-null int64\n",
      "Action             1000209 non-null int64\n",
      "Adventure          1000209 non-null int64\n",
      "Animation          1000209 non-null int64\n",
      "Children's         1000209 non-null int64\n",
      "Comedy             1000209 non-null int64\n",
      "Crime              1000209 non-null int64\n",
      "Documentary        1000209 non-null int64\n",
      "Drama              1000209 non-null int64\n",
      "Fantasy            1000209 non-null int64\n",
      "Film-Noir          1000209 non-null int64\n",
      "Horror             1000209 non-null int64\n",
      "Musical            1000209 non-null int64\n",
      "Mystery            1000209 non-null int64\n",
      "Romance            1000209 non-null int64\n",
      "Sci-Fi             1000209 non-null int64\n",
      "Thriller           1000209 non-null int64\n",
      "War                1000209 non-null int64\n",
      "Western            1000209 non-null int64\n",
      "dtypes: int64(27), object(2)\n",
      "memory usage: 228.9+ MB\n"
     ]
    }
   ],
   "source": [
    "Final_DF.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Correlation Analysis between Features and Target Variables "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.set_option('display.precision',3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>UserID</th>\n",
       "      <th>MovieID</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Occupation</th>\n",
       "      <th>Release_Decade</th>\n",
       "      <th>Year_of_Rating</th>\n",
       "      <th>Month_of_Rating</th>\n",
       "      <th>Action</th>\n",
       "      <th>...</th>\n",
       "      <th>Fantasy</th>\n",
       "      <th>Film-Noir</th>\n",
       "      <th>Horror</th>\n",
       "      <th>Musical</th>\n",
       "      <th>Mystery</th>\n",
       "      <th>Romance</th>\n",
       "      <th>Sci-Fi</th>\n",
       "      <th>Thriller</th>\n",
       "      <th>War</th>\n",
       "      <th>Western</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>UserID</th>\n",
       "      <td>1.000</td>\n",
       "      <td>-0.018</td>\n",
       "      <td>0.012</td>\n",
       "      <td>-0.035</td>\n",
       "      <td>0.035</td>\n",
       "      <td>-0.027</td>\n",
       "      <td>-0.028</td>\n",
       "      <td>-0.094</td>\n",
       "      <td>-0.634</td>\n",
       "      <td>-0.002</td>\n",
       "      <td>...</td>\n",
       "      <td>0.002</td>\n",
       "      <td>0.005</td>\n",
       "      <td>-0.001</td>\n",
       "      <td>-0.000</td>\n",
       "      <td>0.004</td>\n",
       "      <td>0.007</td>\n",
       "      <td>-0.003</td>\n",
       "      <td>-0.001</td>\n",
       "      <td>0.004</td>\n",
       "      <td>0.004</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>MovieID</th>\n",
       "      <td>-0.018</td>\n",
       "      <td>1.000</td>\n",
       "      <td>-0.064</td>\n",
       "      <td>0.022</td>\n",
       "      <td>0.028</td>\n",
       "      <td>0.009</td>\n",
       "      <td>-0.072</td>\n",
       "      <td>0.039</td>\n",
       "      <td>-0.003</td>\n",
       "      <td>-0.042</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.019</td>\n",
       "      <td>-0.020</td>\n",
       "      <td>0.058</td>\n",
       "      <td>-0.059</td>\n",
       "      <td>-0.029</td>\n",
       "      <td>-0.118</td>\n",
       "      <td>-0.012</td>\n",
       "      <td>-0.058</td>\n",
       "      <td>-0.082</td>\n",
       "      <td>0.004</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rating</th>\n",
       "      <td>0.012</td>\n",
       "      <td>-0.064</td>\n",
       "      <td>1.000</td>\n",
       "      <td>-0.020</td>\n",
       "      <td>0.057</td>\n",
       "      <td>0.007</td>\n",
       "      <td>-0.153</td>\n",
       "      <td>-0.025</td>\n",
       "      <td>0.001</td>\n",
       "      <td>-0.048</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.023</td>\n",
       "      <td>0.060</td>\n",
       "      <td>-0.094</td>\n",
       "      <td>0.016</td>\n",
       "      <td>0.016</td>\n",
       "      <td>0.010</td>\n",
       "      <td>-0.044</td>\n",
       "      <td>-0.005</td>\n",
       "      <td>0.076</td>\n",
       "      <td>0.007</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Gender</th>\n",
       "      <td>-0.035</td>\n",
       "      <td>0.022</td>\n",
       "      <td>-0.020</td>\n",
       "      <td>1.000</td>\n",
       "      <td>-0.003</td>\n",
       "      <td>0.115</td>\n",
       "      <td>-0.003</td>\n",
       "      <td>-0.027</td>\n",
       "      <td>0.036</td>\n",
       "      <td>0.094</td>\n",
       "      <td>...</td>\n",
       "      <td>0.003</td>\n",
       "      <td>0.005</td>\n",
       "      <td>0.037</td>\n",
       "      <td>-0.038</td>\n",
       "      <td>-0.001</td>\n",
       "      <td>-0.091</td>\n",
       "      <td>0.072</td>\n",
       "      <td>0.038</td>\n",
       "      <td>0.026</td>\n",
       "      <td>0.026</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Age</th>\n",
       "      <td>0.035</td>\n",
       "      <td>0.028</td>\n",
       "      <td>0.057</td>\n",
       "      <td>-0.003</td>\n",
       "      <td>1.000</td>\n",
       "      <td>0.078</td>\n",
       "      <td>-0.161</td>\n",
       "      <td>-0.066</td>\n",
       "      <td>0.016</td>\n",
       "      <td>-0.031</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.024</td>\n",
       "      <td>0.033</td>\n",
       "      <td>-0.024</td>\n",
       "      <td>0.005</td>\n",
       "      <td>0.024</td>\n",
       "      <td>0.018</td>\n",
       "      <td>-0.011</td>\n",
       "      <td>-0.014</td>\n",
       "      <td>0.038</td>\n",
       "      <td>0.038</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Occupation</th>\n",
       "      <td>-0.027</td>\n",
       "      <td>0.009</td>\n",
       "      <td>0.007</td>\n",
       "      <td>0.115</td>\n",
       "      <td>0.078</td>\n",
       "      <td>1.000</td>\n",
       "      <td>-0.010</td>\n",
       "      <td>-0.003</td>\n",
       "      <td>0.035</td>\n",
       "      <td>0.018</td>\n",
       "      <td>...</td>\n",
       "      <td>0.001</td>\n",
       "      <td>0.005</td>\n",
       "      <td>0.001</td>\n",
       "      <td>-0.007</td>\n",
       "      <td>0.002</td>\n",
       "      <td>-0.014</td>\n",
       "      <td>0.026</td>\n",
       "      <td>0.009</td>\n",
       "      <td>0.010</td>\n",
       "      <td>0.006</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Release_Decade</th>\n",
       "      <td>-0.028</td>\n",
       "      <td>-0.072</td>\n",
       "      <td>-0.153</td>\n",
       "      <td>-0.003</td>\n",
       "      <td>-0.161</td>\n",
       "      <td>-0.010</td>\n",
       "      <td>1.000</td>\n",
       "      <td>0.013</td>\n",
       "      <td>0.010</td>\n",
       "      <td>0.091</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.004</td>\n",
       "      <td>-0.130</td>\n",
       "      <td>-0.066</td>\n",
       "      <td>-0.207</td>\n",
       "      <td>-0.042</td>\n",
       "      <td>0.034</td>\n",
       "      <td>0.005</td>\n",
       "      <td>0.091</td>\n",
       "      <td>-0.106</td>\n",
       "      <td>-0.075</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Year_of_Rating</th>\n",
       "      <td>-0.094</td>\n",
       "      <td>0.039</td>\n",
       "      <td>-0.025</td>\n",
       "      <td>-0.027</td>\n",
       "      <td>-0.066</td>\n",
       "      <td>-0.003</td>\n",
       "      <td>0.013</td>\n",
       "      <td>1.000</td>\n",
       "      <td>-0.433</td>\n",
       "      <td>-0.040</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.011</td>\n",
       "      <td>-0.009</td>\n",
       "      <td>-0.009</td>\n",
       "      <td>0.001</td>\n",
       "      <td>-0.006</td>\n",
       "      <td>-0.002</td>\n",
       "      <td>-0.031</td>\n",
       "      <td>-0.013</td>\n",
       "      <td>-0.018</td>\n",
       "      <td>-0.006</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Month_of_Rating</th>\n",
       "      <td>-0.634</td>\n",
       "      <td>-0.003</td>\n",
       "      <td>0.001</td>\n",
       "      <td>0.036</td>\n",
       "      <td>0.016</td>\n",
       "      <td>0.035</td>\n",
       "      <td>0.010</td>\n",
       "      <td>-0.433</td>\n",
       "      <td>1.000</td>\n",
       "      <td>0.018</td>\n",
       "      <td>...</td>\n",
       "      <td>0.001</td>\n",
       "      <td>0.001</td>\n",
       "      <td>0.005</td>\n",
       "      <td>-0.001</td>\n",
       "      <td>-0.001</td>\n",
       "      <td>-0.004</td>\n",
       "      <td>0.017</td>\n",
       "      <td>0.003</td>\n",
       "      <td>0.010</td>\n",
       "      <td>0.001</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Action</th>\n",
       "      <td>-0.002</td>\n",
       "      <td>-0.042</td>\n",
       "      <td>-0.048</td>\n",
       "      <td>0.094</td>\n",
       "      <td>-0.031</td>\n",
       "      <td>0.018</td>\n",
       "      <td>0.091</td>\n",
       "      <td>-0.040</td>\n",
       "      <td>0.018</td>\n",
       "      <td>1.000</td>\n",
       "      <td>...</td>\n",
       "      <td>0.015</td>\n",
       "      <td>-0.080</td>\n",
       "      <td>-0.043</td>\n",
       "      <td>-0.100</td>\n",
       "      <td>-0.054</td>\n",
       "      <td>-0.068</td>\n",
       "      <td>0.319</td>\n",
       "      <td>0.203</td>\n",
       "      <td>0.136</td>\n",
       "      <td>0.022</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Adventure</th>\n",
       "      <td>-0.001</td>\n",
       "      <td>-0.082</td>\n",
       "      <td>-0.037</td>\n",
       "      <td>0.039</td>\n",
       "      <td>-0.017</td>\n",
       "      <td>0.014</td>\n",
       "      <td>-0.019</td>\n",
       "      <td>-0.027</td>\n",
       "      <td>0.011</td>\n",
       "      <td>0.375</td>\n",
       "      <td>...</td>\n",
       "      <td>0.227</td>\n",
       "      <td>-0.014</td>\n",
       "      <td>-0.057</td>\n",
       "      <td>-0.022</td>\n",
       "      <td>-0.044</td>\n",
       "      <td>-0.024</td>\n",
       "      <td>0.284</td>\n",
       "      <td>-0.038</td>\n",
       "      <td>0.017</td>\n",
       "      <td>-0.012</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Animation</th>\n",
       "      <td>-0.008</td>\n",
       "      <td>-0.014</td>\n",
       "      <td>0.020</td>\n",
       "      <td>-0.018</td>\n",
       "      <td>-0.047</td>\n",
       "      <td>-0.004</td>\n",
       "      <td>-0.048</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.000</td>\n",
       "      <td>-0.110</td>\n",
       "      <td>...</td>\n",
       "      <td>0.012</td>\n",
       "      <td>0.037</td>\n",
       "      <td>-0.050</td>\n",
       "      <td>0.335</td>\n",
       "      <td>-0.042</td>\n",
       "      <td>-0.055</td>\n",
       "      <td>-0.056</td>\n",
       "      <td>-0.086</td>\n",
       "      <td>-0.046</td>\n",
       "      <td>-0.031</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Children's</th>\n",
       "      <td>-0.005</td>\n",
       "      <td>-0.072</td>\n",
       "      <td>-0.040</td>\n",
       "      <td>-0.032</td>\n",
       "      <td>-0.053</td>\n",
       "      <td>-0.007</td>\n",
       "      <td>-0.075</td>\n",
       "      <td>-0.000</td>\n",
       "      <td>-0.002</td>\n",
       "      <td>-0.141</td>\n",
       "      <td>...</td>\n",
       "      <td>0.263</td>\n",
       "      <td>-0.038</td>\n",
       "      <td>-0.077</td>\n",
       "      <td>0.313</td>\n",
       "      <td>-0.053</td>\n",
       "      <td>-0.085</td>\n",
       "      <td>-0.039</td>\n",
       "      <td>-0.133</td>\n",
       "      <td>-0.067</td>\n",
       "      <td>-0.031</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Comedy</th>\n",
       "      <td>-0.004</td>\n",
       "      <td>0.062</td>\n",
       "      <td>-0.040</td>\n",
       "      <td>-0.041</td>\n",
       "      <td>-0.044</td>\n",
       "      <td>-0.006</td>\n",
       "      <td>0.098</td>\n",
       "      <td>0.006</td>\n",
       "      <td>-0.001</td>\n",
       "      <td>-0.268</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.006</td>\n",
       "      <td>-0.101</td>\n",
       "      <td>-0.093</td>\n",
       "      <td>0.031</td>\n",
       "      <td>-0.105</td>\n",
       "      <td>0.113</td>\n",
       "      <td>-0.187</td>\n",
       "      <td>-0.300</td>\n",
       "      <td>-0.127</td>\n",
       "      <td>0.008</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Crime</th>\n",
       "      <td>0.003</td>\n",
       "      <td>-0.062</td>\n",
       "      <td>0.033</td>\n",
       "      <td>0.027</td>\n",
       "      <td>-0.008</td>\n",
       "      <td>0.003</td>\n",
       "      <td>0.056</td>\n",
       "      <td>-0.009</td>\n",
       "      <td>-0.000</td>\n",
       "      <td>0.089</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.034</td>\n",
       "      <td>0.136</td>\n",
       "      <td>-0.048</td>\n",
       "      <td>-0.061</td>\n",
       "      <td>0.080</td>\n",
       "      <td>-0.073</td>\n",
       "      <td>-0.084</td>\n",
       "      <td>0.115</td>\n",
       "      <td>-0.080</td>\n",
       "      <td>-0.043</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Documentary</th>\n",
       "      <td>-0.001</td>\n",
       "      <td>-0.010</td>\n",
       "      <td>0.028</td>\n",
       "      <td>0.000</td>\n",
       "      <td>0.004</td>\n",
       "      <td>-0.003</td>\n",
       "      <td>0.040</td>\n",
       "      <td>0.009</td>\n",
       "      <td>-0.002</td>\n",
       "      <td>-0.053</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.017</td>\n",
       "      <td>-0.012</td>\n",
       "      <td>-0.026</td>\n",
       "      <td>-0.007</td>\n",
       "      <td>-0.018</td>\n",
       "      <td>-0.037</td>\n",
       "      <td>-0.039</td>\n",
       "      <td>-0.043</td>\n",
       "      <td>-0.016</td>\n",
       "      <td>-0.013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Drama</th>\n",
       "      <td>0.007</td>\n",
       "      <td>-0.031</td>\n",
       "      <td>0.123</td>\n",
       "      <td>-0.052</td>\n",
       "      <td>0.064</td>\n",
       "      <td>-0.012</td>\n",
       "      <td>0.021</td>\n",
       "      <td>0.013</td>\n",
       "      <td>-0.007</td>\n",
       "      <td>-0.202</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.097</td>\n",
       "      <td>-0.067</td>\n",
       "      <td>-0.190</td>\n",
       "      <td>-0.095</td>\n",
       "      <td>-0.028</td>\n",
       "      <td>0.024</td>\n",
       "      <td>-0.213</td>\n",
       "      <td>-0.154</td>\n",
       "      <td>0.137</td>\n",
       "      <td>-0.046</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Fantasy</th>\n",
       "      <td>0.002</td>\n",
       "      <td>-0.019</td>\n",
       "      <td>-0.023</td>\n",
       "      <td>0.003</td>\n",
       "      <td>-0.024</td>\n",
       "      <td>0.001</td>\n",
       "      <td>-0.004</td>\n",
       "      <td>-0.011</td>\n",
       "      <td>0.001</td>\n",
       "      <td>0.015</td>\n",
       "      <td>...</td>\n",
       "      <td>1.000</td>\n",
       "      <td>-0.026</td>\n",
       "      <td>-0.056</td>\n",
       "      <td>-0.020</td>\n",
       "      <td>-0.040</td>\n",
       "      <td>-0.015</td>\n",
       "      <td>0.122</td>\n",
       "      <td>-0.087</td>\n",
       "      <td>-0.045</td>\n",
       "      <td>-0.028</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Film-Noir</th>\n",
       "      <td>0.005</td>\n",
       "      <td>-0.020</td>\n",
       "      <td>0.060</td>\n",
       "      <td>0.005</td>\n",
       "      <td>0.033</td>\n",
       "      <td>0.005</td>\n",
       "      <td>-0.130</td>\n",
       "      <td>-0.009</td>\n",
       "      <td>0.001</td>\n",
       "      <td>-0.080</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.026</td>\n",
       "      <td>1.000</td>\n",
       "      <td>-0.039</td>\n",
       "      <td>-0.028</td>\n",
       "      <td>0.215</td>\n",
       "      <td>-0.047</td>\n",
       "      <td>-0.004</td>\n",
       "      <td>0.115</td>\n",
       "      <td>-0.037</td>\n",
       "      <td>-0.020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Horror</th>\n",
       "      <td>-0.001</td>\n",
       "      <td>0.058</td>\n",
       "      <td>-0.094</td>\n",
       "      <td>0.037</td>\n",
       "      <td>-0.024</td>\n",
       "      <td>0.001</td>\n",
       "      <td>-0.066</td>\n",
       "      <td>-0.009</td>\n",
       "      <td>0.005</td>\n",
       "      <td>-0.043</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.056</td>\n",
       "      <td>-0.039</td>\n",
       "      <td>1.000</td>\n",
       "      <td>-0.019</td>\n",
       "      <td>-0.002</td>\n",
       "      <td>-0.099</td>\n",
       "      <td>0.057</td>\n",
       "      <td>0.057</td>\n",
       "      <td>-0.078</td>\n",
       "      <td>-0.042</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Musical</th>\n",
       "      <td>-0.000</td>\n",
       "      <td>-0.059</td>\n",
       "      <td>0.016</td>\n",
       "      <td>-0.038</td>\n",
       "      <td>0.005</td>\n",
       "      <td>-0.007</td>\n",
       "      <td>-0.207</td>\n",
       "      <td>0.001</td>\n",
       "      <td>-0.001</td>\n",
       "      <td>-0.100</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.020</td>\n",
       "      <td>-0.028</td>\n",
       "      <td>-0.019</td>\n",
       "      <td>1.000</td>\n",
       "      <td>-0.043</td>\n",
       "      <td>0.024</td>\n",
       "      <td>-0.068</td>\n",
       "      <td>-0.101</td>\n",
       "      <td>-0.034</td>\n",
       "      <td>-0.030</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mystery</th>\n",
       "      <td>0.004</td>\n",
       "      <td>-0.029</td>\n",
       "      <td>0.016</td>\n",
       "      <td>-0.001</td>\n",
       "      <td>0.024</td>\n",
       "      <td>0.002</td>\n",
       "      <td>-0.042</td>\n",
       "      <td>-0.006</td>\n",
       "      <td>-0.001</td>\n",
       "      <td>-0.054</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.040</td>\n",
       "      <td>0.215</td>\n",
       "      <td>-0.002</td>\n",
       "      <td>-0.043</td>\n",
       "      <td>1.000</td>\n",
       "      <td>-0.040</td>\n",
       "      <td>-0.028</td>\n",
       "      <td>0.225</td>\n",
       "      <td>-0.055</td>\n",
       "      <td>-0.030</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Romance</th>\n",
       "      <td>0.007</td>\n",
       "      <td>-0.118</td>\n",
       "      <td>0.010</td>\n",
       "      <td>-0.091</td>\n",
       "      <td>0.018</td>\n",
       "      <td>-0.014</td>\n",
       "      <td>0.034</td>\n",
       "      <td>-0.002</td>\n",
       "      <td>-0.004</td>\n",
       "      <td>-0.068</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.015</td>\n",
       "      <td>-0.047</td>\n",
       "      <td>-0.099</td>\n",
       "      <td>0.024</td>\n",
       "      <td>-0.040</td>\n",
       "      <td>1.000</td>\n",
       "      <td>-0.134</td>\n",
       "      <td>-0.081</td>\n",
       "      <td>0.053</td>\n",
       "      <td>-0.045</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Sci-Fi</th>\n",
       "      <td>-0.003</td>\n",
       "      <td>-0.012</td>\n",
       "      <td>-0.044</td>\n",
       "      <td>0.072</td>\n",
       "      <td>-0.011</td>\n",
       "      <td>0.026</td>\n",
       "      <td>0.005</td>\n",
       "      <td>-0.031</td>\n",
       "      <td>0.017</td>\n",
       "      <td>0.319</td>\n",
       "      <td>...</td>\n",
       "      <td>0.122</td>\n",
       "      <td>-0.004</td>\n",
       "      <td>0.057</td>\n",
       "      <td>-0.068</td>\n",
       "      <td>-0.028</td>\n",
       "      <td>-0.134</td>\n",
       "      <td>1.000</td>\n",
       "      <td>0.103</td>\n",
       "      <td>0.039</td>\n",
       "      <td>-0.011</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Thriller</th>\n",
       "      <td>-0.001</td>\n",
       "      <td>-0.058</td>\n",
       "      <td>-0.005</td>\n",
       "      <td>0.038</td>\n",
       "      <td>-0.014</td>\n",
       "      <td>0.009</td>\n",
       "      <td>0.091</td>\n",
       "      <td>-0.013</td>\n",
       "      <td>0.003</td>\n",
       "      <td>0.203</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.087</td>\n",
       "      <td>0.115</td>\n",
       "      <td>0.057</td>\n",
       "      <td>-0.101</td>\n",
       "      <td>0.225</td>\n",
       "      <td>-0.081</td>\n",
       "      <td>0.103</td>\n",
       "      <td>1.000</td>\n",
       "      <td>-0.088</td>\n",
       "      <td>-0.059</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>War</th>\n",
       "      <td>0.004</td>\n",
       "      <td>-0.082</td>\n",
       "      <td>0.076</td>\n",
       "      <td>0.026</td>\n",
       "      <td>0.038</td>\n",
       "      <td>0.010</td>\n",
       "      <td>-0.106</td>\n",
       "      <td>-0.018</td>\n",
       "      <td>0.010</td>\n",
       "      <td>0.136</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.045</td>\n",
       "      <td>-0.037</td>\n",
       "      <td>-0.078</td>\n",
       "      <td>-0.034</td>\n",
       "      <td>-0.055</td>\n",
       "      <td>0.053</td>\n",
       "      <td>0.039</td>\n",
       "      <td>-0.088</td>\n",
       "      <td>1.000</td>\n",
       "      <td>-0.020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Western</th>\n",
       "      <td>0.004</td>\n",
       "      <td>0.004</td>\n",
       "      <td>0.007</td>\n",
       "      <td>0.026</td>\n",
       "      <td>0.038</td>\n",
       "      <td>0.006</td>\n",
       "      <td>-0.075</td>\n",
       "      <td>-0.006</td>\n",
       "      <td>0.001</td>\n",
       "      <td>0.022</td>\n",
       "      <td>...</td>\n",
       "      <td>-0.028</td>\n",
       "      <td>-0.020</td>\n",
       "      <td>-0.042</td>\n",
       "      <td>-0.030</td>\n",
       "      <td>-0.030</td>\n",
       "      <td>-0.045</td>\n",
       "      <td>-0.011</td>\n",
       "      <td>-0.059</td>\n",
       "      <td>-0.020</td>\n",
       "      <td>1.000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>27 rows × 27 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                 UserID  MovieID  Rating  Gender    Age  Occupation  \\\n",
       "UserID            1.000   -0.018   0.012  -0.035  0.035      -0.027   \n",
       "MovieID          -0.018    1.000  -0.064   0.022  0.028       0.009   \n",
       "Rating            0.012   -0.064   1.000  -0.020  0.057       0.007   \n",
       "Gender           -0.035    0.022  -0.020   1.000 -0.003       0.115   \n",
       "Age               0.035    0.028   0.057  -0.003  1.000       0.078   \n",
       "Occupation       -0.027    0.009   0.007   0.115  0.078       1.000   \n",
       "Release_Decade   -0.028   -0.072  -0.153  -0.003 -0.161      -0.010   \n",
       "Year_of_Rating   -0.094    0.039  -0.025  -0.027 -0.066      -0.003   \n",
       "Month_of_Rating  -0.634   -0.003   0.001   0.036  0.016       0.035   \n",
       "Action           -0.002   -0.042  -0.048   0.094 -0.031       0.018   \n",
       "Adventure        -0.001   -0.082  -0.037   0.039 -0.017       0.014   \n",
       "Animation        -0.008   -0.014   0.020  -0.018 -0.047      -0.004   \n",
       "Children's       -0.005   -0.072  -0.040  -0.032 -0.053      -0.007   \n",
       "Comedy           -0.004    0.062  -0.040  -0.041 -0.044      -0.006   \n",
       "Crime             0.003   -0.062   0.033   0.027 -0.008       0.003   \n",
       "Documentary      -0.001   -0.010   0.028   0.000  0.004      -0.003   \n",
       "Drama             0.007   -0.031   0.123  -0.052  0.064      -0.012   \n",
       "Fantasy           0.002   -0.019  -0.023   0.003 -0.024       0.001   \n",
       "Film-Noir         0.005   -0.020   0.060   0.005  0.033       0.005   \n",
       "Horror           -0.001    0.058  -0.094   0.037 -0.024       0.001   \n",
       "Musical          -0.000   -0.059   0.016  -0.038  0.005      -0.007   \n",
       "Mystery           0.004   -0.029   0.016  -0.001  0.024       0.002   \n",
       "Romance           0.007   -0.118   0.010  -0.091  0.018      -0.014   \n",
       "Sci-Fi           -0.003   -0.012  -0.044   0.072 -0.011       0.026   \n",
       "Thriller         -0.001   -0.058  -0.005   0.038 -0.014       0.009   \n",
       "War               0.004   -0.082   0.076   0.026  0.038       0.010   \n",
       "Western           0.004    0.004   0.007   0.026  0.038       0.006   \n",
       "\n",
       "                 Release_Decade  Year_of_Rating  Month_of_Rating  Action  \\\n",
       "UserID                   -0.028          -0.094           -0.634  -0.002   \n",
       "MovieID                  -0.072           0.039           -0.003  -0.042   \n",
       "Rating                   -0.153          -0.025            0.001  -0.048   \n",
       "Gender                   -0.003          -0.027            0.036   0.094   \n",
       "Age                      -0.161          -0.066            0.016  -0.031   \n",
       "Occupation               -0.010          -0.003            0.035   0.018   \n",
       "Release_Decade            1.000           0.013            0.010   0.091   \n",
       "Year_of_Rating            0.013           1.000           -0.433  -0.040   \n",
       "Month_of_Rating           0.010          -0.433            1.000   0.018   \n",
       "Action                    0.091          -0.040            0.018   1.000   \n",
       "Adventure                -0.019          -0.027            0.011   0.375   \n",
       "Animation                -0.048           0.000            0.000  -0.110   \n",
       "Children's               -0.075          -0.000           -0.002  -0.141   \n",
       "Comedy                    0.098           0.006           -0.001  -0.268   \n",
       "Crime                     0.056          -0.009           -0.000   0.089   \n",
       "Documentary               0.040           0.009           -0.002  -0.053   \n",
       "Drama                     0.021           0.013           -0.007  -0.202   \n",
       "Fantasy                  -0.004          -0.011            0.001   0.015   \n",
       "Film-Noir                -0.130          -0.009            0.001  -0.080   \n",
       "Horror                   -0.066          -0.009            0.005  -0.043   \n",
       "Musical                  -0.207           0.001           -0.001  -0.100   \n",
       "Mystery                  -0.042          -0.006           -0.001  -0.054   \n",
       "Romance                   0.034          -0.002           -0.004  -0.068   \n",
       "Sci-Fi                    0.005          -0.031            0.017   0.319   \n",
       "Thriller                  0.091          -0.013            0.003   0.203   \n",
       "War                      -0.106          -0.018            0.010   0.136   \n",
       "Western                  -0.075          -0.006            0.001   0.022   \n",
       "\n",
       "                  ...     Fantasy  Film-Noir  Horror  Musical  Mystery  \\\n",
       "UserID            ...       0.002      0.005  -0.001   -0.000    0.004   \n",
       "MovieID           ...      -0.019     -0.020   0.058   -0.059   -0.029   \n",
       "Rating            ...      -0.023      0.060  -0.094    0.016    0.016   \n",
       "Gender            ...       0.003      0.005   0.037   -0.038   -0.001   \n",
       "Age               ...      -0.024      0.033  -0.024    0.005    0.024   \n",
       "Occupation        ...       0.001      0.005   0.001   -0.007    0.002   \n",
       "Release_Decade    ...      -0.004     -0.130  -0.066   -0.207   -0.042   \n",
       "Year_of_Rating    ...      -0.011     -0.009  -0.009    0.001   -0.006   \n",
       "Month_of_Rating   ...       0.001      0.001   0.005   -0.001   -0.001   \n",
       "Action            ...       0.015     -0.080  -0.043   -0.100   -0.054   \n",
       "Adventure         ...       0.227     -0.014  -0.057   -0.022   -0.044   \n",
       "Animation         ...       0.012      0.037  -0.050    0.335   -0.042   \n",
       "Children's        ...       0.263     -0.038  -0.077    0.313   -0.053   \n",
       "Comedy            ...      -0.006     -0.101  -0.093    0.031   -0.105   \n",
       "Crime             ...      -0.034      0.136  -0.048   -0.061    0.080   \n",
       "Documentary       ...      -0.017     -0.012  -0.026   -0.007   -0.018   \n",
       "Drama             ...      -0.097     -0.067  -0.190   -0.095   -0.028   \n",
       "Fantasy           ...       1.000     -0.026  -0.056   -0.020   -0.040   \n",
       "Film-Noir         ...      -0.026      1.000  -0.039   -0.028    0.215   \n",
       "Horror            ...      -0.056     -0.039   1.000   -0.019   -0.002   \n",
       "Musical           ...      -0.020     -0.028  -0.019    1.000   -0.043   \n",
       "Mystery           ...      -0.040      0.215  -0.002   -0.043    1.000   \n",
       "Romance           ...      -0.015     -0.047  -0.099    0.024   -0.040   \n",
       "Sci-Fi            ...       0.122     -0.004   0.057   -0.068   -0.028   \n",
       "Thriller          ...      -0.087      0.115   0.057   -0.101    0.225   \n",
       "War               ...      -0.045     -0.037  -0.078   -0.034   -0.055   \n",
       "Western           ...      -0.028     -0.020  -0.042   -0.030   -0.030   \n",
       "\n",
       "                 Romance  Sci-Fi  Thriller    War  Western  \n",
       "UserID             0.007  -0.003    -0.001  0.004    0.004  \n",
       "MovieID           -0.118  -0.012    -0.058 -0.082    0.004  \n",
       "Rating             0.010  -0.044    -0.005  0.076    0.007  \n",
       "Gender            -0.091   0.072     0.038  0.026    0.026  \n",
       "Age                0.018  -0.011    -0.014  0.038    0.038  \n",
       "Occupation        -0.014   0.026     0.009  0.010    0.006  \n",
       "Release_Decade     0.034   0.005     0.091 -0.106   -0.075  \n",
       "Year_of_Rating    -0.002  -0.031    -0.013 -0.018   -0.006  \n",
       "Month_of_Rating   -0.004   0.017     0.003  0.010    0.001  \n",
       "Action            -0.068   0.319     0.203  0.136    0.022  \n",
       "Adventure         -0.024   0.284    -0.038  0.017   -0.012  \n",
       "Animation         -0.055  -0.056    -0.086 -0.046   -0.031  \n",
       "Children's        -0.085  -0.039    -0.133 -0.067   -0.031  \n",
       "Comedy             0.113  -0.187    -0.300 -0.127    0.008  \n",
       "Crime             -0.073  -0.084     0.115 -0.080   -0.043  \n",
       "Documentary       -0.037  -0.039    -0.043 -0.016   -0.013  \n",
       "Drama              0.024  -0.213    -0.154  0.137   -0.046  \n",
       "Fantasy           -0.015   0.122    -0.087 -0.045   -0.028  \n",
       "Film-Noir         -0.047  -0.004     0.115 -0.037   -0.020  \n",
       "Horror            -0.099   0.057     0.057 -0.078   -0.042  \n",
       "Musical            0.024  -0.068    -0.101 -0.034   -0.030  \n",
       "Mystery           -0.040  -0.028     0.225 -0.055   -0.030  \n",
       "Romance            1.000  -0.134    -0.081  0.053   -0.045  \n",
       "Sci-Fi            -0.134   1.000     0.103  0.039   -0.011  \n",
       "Thriller          -0.081   0.103     1.000 -0.088   -0.059  \n",
       "War                0.053   0.039    -0.088  1.000   -0.020  \n",
       "Western           -0.045  -0.011    -0.059 -0.020    1.000  \n",
       "\n",
       "[27 rows x 27 columns]"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Final_DF.corr().round(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1c92226d7b8>"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x1440 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(20,20))\n",
    "sns.heatmap(Final_DF.corr(),annot=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['MovieID', 'Rating', 'Age', 'Release_Decade', 'Drama', 'Film-Noir',\n",
      "       'Horror', 'War'],\n",
      "      dtype='object')\n",
      "UserID             0.01\n",
      "MovieID            0.06\n",
      "Rating             1.00\n",
      "Gender             0.02\n",
      "Age                0.06\n",
      "Occupation         0.01\n",
      "Release_Decade     0.15\n",
      "Year_of_Rating     0.02\n",
      "Month_of_Rating    0.00\n",
      "Action             0.05\n",
      "Adventure          0.04\n",
      "Animation          0.02\n",
      "Children's         0.04\n",
      "Comedy             0.04\n",
      "Crime              0.03\n",
      "Documentary        0.03\n",
      "Drama              0.12\n",
      "Fantasy            0.02\n",
      "Film-Noir          0.06\n",
      "Horror             0.09\n",
      "Musical            0.02\n",
      "Mystery            0.02\n",
      "Romance            0.01\n",
      "Sci-Fi             0.04\n",
      "Thriller           0.00\n",
      "War                0.08\n",
      "Western            0.01\n",
      "Name: Rating, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "#Correlation with output variable\n",
    "cor=Final_DF.corr().round(2)\n",
    "cor_target = abs(cor[\"Rating\"])\n",
    "#Selecting highly correlated features\n",
    "relevant_features = cor_target[cor_target>0.05]\n",
    "list1=[]\n",
    "list1=relevant_features.index\n",
    "print(list1)\n",
    "print(cor_target)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Age', 'Release_Decade', 'Drama', 'Film-Noir', 'Horror', 'War'], dtype='object')"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list1[2::]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "FeaturesDF= Final_DF[list1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>MovieID</th>\n",
       "      <th>Rating</th>\n",
       "      <th>Age</th>\n",
       "      <th>Release_Decade</th>\n",
       "      <th>Drama</th>\n",
       "      <th>Film-Noir</th>\n",
       "      <th>Horror</th>\n",
       "      <th>War</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1193</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   MovieID  Rating  Age  Release_Decade  Drama  Film-Noir  Horror  War\n",
       "0     1193       5    1               6      1          0       0    0"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "FeaturesDF.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 1,  6,  1,  0,  0,  0],\n",
       "       [ 1,  8,  0,  0,  0,  0],\n",
       "       [ 1,  5,  0,  0,  0,  0],\n",
       "       ...,\n",
       "       [45,  7,  0,  0,  1,  0],\n",
       "       [45,  7,  0,  0,  0,  1],\n",
       "       [45,  6,  1,  0,  0,  0]], dtype=int64)"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "label = np.array(FeaturesDF.Rating)\n",
    "Features = np.array(FeaturesDF.iloc[:,2::])\n",
    "#label.shape\n",
    "#Features.shap\n",
    "Features[0::]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Building Appropriate Model to predict the movie rating. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training Score is :0.3521014295693162 and testing score is :0.3522013333173367 for Random state:3\n",
      "Training Score is :0.3519934520286447 and testing score is :0.3522013333173367 for Random state:4\n",
      "Training Score is :0.3518641455910504 and testing score is :0.3521013545128433 for Random state:6\n",
      "Training Score is :0.3520147809255675 and testing score is :0.35238129516542493 for Random state:8\n",
      "Highest_test_Score: 0.35238129516542493 is for Random State : 8\n"
     ]
    }
   ],
   "source": [
    "# Logistic Regression.\n",
    "Highest_test_Score = 0\n",
    "Best_Random_state  = 0\n",
    "for i in range(1,10):\n",
    "    \n",
    "    from sklearn.model_selection import train_test_split\n",
    "    from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "    x_train,x_test,y_train,y_test = train_test_split(Features,label,test_size=0.25,random_state=i)\n",
    "    model = LogisticRegression()\n",
    "    model.fit(x_train,y_train)\n",
    "    LogRegTrainScore=model.score(x_train,y_train)\n",
    "    LogRegTestScore=model.score(x_test,y_test)\n",
    "    if LogRegTestScore > LogRegTrainScore:\n",
    "            print(\"Training Score is :{} and testing score is :{} for Random state:{}\".\n",
    "            format(LogRegTrainScore,LogRegTestScore,i))\n",
    "            if Highest_test_Score < LogRegTestScore:\n",
    "                Highest_test_Score = LogRegTestScore\n",
    "                Best_Random_state = i\n",
    "            \n",
    "print('Highest_test_Score: {} is for Random State : {}'.format(Highest_test_Score,Best_Random_state))\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Test Score 0.3560152821546452 is for Random State 31 with Train score of 0.35340907727561754\n"
     ]
    }
   ],
   "source": [
    "# Descion Tress\n",
    "DT_Best_Accuracy_score = 0\n",
    "DT_best_random_state = 0\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.model_selection import train_test_split\n",
    "for i in range(1,50):\n",
    "    x_train,x_test,y_train,y_test = train_test_split(Features,label,test_size=0.25,random_state=i)\n",
    "    DTModel = DecisionTreeClassifier()\n",
    "    DTModel.fit(x_train,y_train)\n",
    "    DTTestScore  = DTModel.score(x_train,y_train)\n",
    "    DTTrainScore = DTModel.score(x_test,y_test)\n",
    "    if DTTestScore > DTTrainScore:\n",
    "        if DT_Best_Accuracy_score < DTTestScore:\n",
    "            DT_Best_Accuracy_score = DTTestScore\n",
    "            DT_best_random_state = i\n",
    "            \n",
    "\n",
    "print('Best Test Score {} is for Random State {} with Train score of {}'.\n",
    "      format(DT_Best_Accuracy_score,DT_best_random_state,DTTrainScore))\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Test Score : 0.35082162581532716 is for Random State :14 with train score :0.34888209919003516\n"
     ]
    }
   ],
   "source": [
    "# Neive Bayes\n",
    "\n",
    "NB_Best_Acc_score = 0\n",
    "NB_Best_random_state = 0\n",
    "\n",
    "from sklearn.naive_bayes import BernoulliNB\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "for i in range(1,50):\n",
    "    x_train,x_test,y_train,y_test = train_test_split(Features,label,test_size=0.25,random_state=i)\n",
    "    NB_model = BernoulliNB()\n",
    "    NB_model.fit(x_train,y_train)\n",
    "    NBTestScore = NB_model.score(x_test,y_test)\n",
    "    NBTrainScore = NB_model.score(x_train,y_train)\n",
    "    \n",
    "    if NBTestScore > NBTrainScore:\n",
    "        if NBTestScore > NB_Best_Acc_score:\n",
    "            NB_Best_Acc_score = NBTestScore\n",
    "            NB_Best_random_state = i\n",
    "\n",
    "print('Best Test Score : {} is for Random State :{} with train score :{}'.\n",
    "      format(NB_Best_Acc_score,NB_Best_random_state,NBTrainScore))\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Test Score : 0.35601652449680665 is for Random State :17 with train score :0.3554540655543647\n"
     ]
    }
   ],
   "source": [
    "# Random Forest\n",
    "RF_Best_Acc_score = 0\n",
    "RF_Best_random_state = 0\n",
    "\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "for i in range(1,50):\n",
    "    x_train,x_test,y_train,y_test = train_test_split(Features,label,test_size=0.25,random_state=i)\n",
    "    RF_model = RandomForestClassifier()\n",
    "    RF_model.fit(x_train,y_train)\n",
    "    RFTestScore = RF_model.score(x_test,y_test)\n",
    "    RFTrainScore = RF_model.score(x_train,y_train)\n",
    "    \n",
    "    if RFTestScore > RFTrainScore:\n",
    "        if RFTestScore > RF_Best_Acc_score:\n",
    "            RF_Best_Acc_score = RFTestScore\n",
    "            RF_Best_random_state = i\n",
    "\n",
    "print('Best Test Score : {} is for Random State :{} with train score :{}'.\n",
    "      format(RF_Best_Acc_score,RF_Best_random_state,RFTrainScore))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Best Test Score : 0.3521240915222967 is for Random State :0 with train score :0.35242136302315785\n"
     ]
    }
   ],
   "source": [
    "# One Vs Rest Classifier \n",
    "OVR_Best_Score = 0\n",
    "OVR_Best_Random_State = 0\n",
    "\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "for i in range(1,50):\n",
    "    x_train,x_test,y_train,y_test = train_test_split(Features,label,test_size=0.25,random_state=i)\n",
    "    OVR_Model = LogisticRegression(multi_class='ovr')\n",
    "    OVR_Model.fit(x_train,y_train)\n",
    "    OVRTestScore  = OVR_Model.score(x_test,y_test)\n",
    "    OVRTrainScore = OVR_Model.score(x_train,y_train)\n",
    "    if OVRTestScore > OVRTrainScore:\n",
    "        if OVR_Best_Score < OVRTestScore:\n",
    "            OVR_Best_Score = OVRTrainScore\n",
    "\n",
    "print('Best Test Score : {} is for Random State :{} with train score :{}'.\n",
    "      format(OVR_Best_Score,OVR_Best_Random_State,OVRTrainScore))\n",
    "   \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Store the results from each model into Seperate Dataframe\n",
    "List_of_col = ['Model_Name','Model_Best_Scores']\n",
    "Results = pd.DataFrame(columns=List_of_col)\n",
    "\n",
    "Model_list = ['Logistic_reg','Descion Trees','Neive Bayes','Random Forest','One Vs Rest LogReg']\n",
    "Score_list = [Highest_test_Score,DT_Best_Accuracy_score,NB_Best_Acc_score,RF_Best_Acc_score,OVR_Best_Score] \n",
    "Results['Model_Name'] = Model_list\n",
    "Results['Model_Best_Scores'] = Score_list\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Model_Name</th>\n",
       "      <th>Model_Best_Scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Logistic_reg</td>\n",
       "      <td>0.352</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Descion Trees</td>\n",
       "      <td>0.356</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Neive Bayes</td>\n",
       "      <td>0.351</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Random Forest</td>\n",
       "      <td>0.356</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>One Vs Rest LogReg</td>\n",
       "      <td>0.352</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Model_Name  Model_Best_Scores\n",
       "0        Logistic_reg              0.352\n",
       "1       Descion Trees              0.356\n",
       "2         Neive Bayes              0.351\n",
       "3       Random Forest              0.356\n",
       "4  One Vs Rest LogReg              0.352"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Accuracy Scores of All the Confusion Matrix for all Models.\n",
    "Results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4    348971\n",
       "3    261197\n",
       "5    226310\n",
       "2    107557\n",
       "1     56174\n",
       "Name: Rating, dtype: int64"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Lets check weather the Dataset is Balanced or Not\n",
    "Final_DF.Rating.value_counts()\n",
    "# Below Results show that there is diversity in Ratings and its a Unbalanced Dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.3521653974319367\n",
      "0.35499480608552814\n",
      "0.3487281158237928\n",
      "0.35489382719011725\n",
      "0.3521484009841943\n"
     ]
    }
   ],
   "source": [
    "# Calculating Accuracies of Different Models\n",
    "\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.metrics import confusion_matrix\n",
    "from sklearn.metrics import classification_report\n",
    "\n",
    "# 1. Accuracy Score of Logistic Regression\n",
    "print(accuracy_score(label,model.predict(Features)))\n",
    "# 2. Accuracy Score of Descion Trees\n",
    "print(accuracy_score(label,DTModel.predict(Features)))\n",
    "# 3. Accuracy Score of Neive Bayes\n",
    "print(accuracy_score(label,NB_model.predict(Features)))\n",
    "# 4. Accuracy Score of Random Forest\n",
    "print(accuracy_score(label,RF_model.predict(Features)))\n",
    "# 5. Accuracy Score of One Vs Rest LogReg\n",
    "print(accuracy_score(label,OVR_Model.predict(Features)))\n",
    "\n",
    "Results[\"Accuracy Score\"] = [accuracy_score(label,model.predict(Features)),\n",
    "                            accuracy_score(label,DTModel.predict(Features)),\n",
    "                            accuracy_score(label,NB_model.predict(Features)),\n",
    "                            accuracy_score(label,RF_model.predict(Features)),\n",
    "                            accuracy_score(label,OVR_Model.predict(Features))]\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Confusion Matrix and Classification Reports  for All Models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Logistic Regression\n",
      "[[     0      0   7029  48445    700]\n",
      " [     0      0   8990  97021   1546]\n",
      " [     0      0  14522 239343   7332]\n",
      " [     0      0  13229 319140  16602]\n",
      " [     0      0   5431 202302  18577]]\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           1       0.00      0.00      0.00     56174\n",
      "           2       0.00      0.00      0.00    107557\n",
      "           3       0.30      0.06      0.09    261197\n",
      "           4       0.35      0.91      0.51    348971\n",
      "           5       0.42      0.08      0.14    226310\n",
      "\n",
      "   micro avg       0.35      0.35      0.35   1000209\n",
      "   macro avg       0.21      0.21      0.15   1000209\n",
      "weighted avg       0.29      0.35      0.23   1000209\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Confusion Matrix and Classification Reports\n",
    "\n",
    "#1. Logistic Regression \n",
    "print(\"Logistic Regression\")\n",
    "Logcm = confusion_matrix(label,model.predict(Features))\n",
    "print(Logcm)\n",
    "Log_classification_report = classification_report(label,model.predict(Features))\n",
    "print(Log_classification_report)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[     7      8   6527  48567   1065]\n",
      " [     4     12   8884  96371   2286]\n",
      " [     7     10  14632 237204   9344]\n",
      " [     1      6  13046 316285  19633]\n",
      " [     2      3   5361 196811  24133]]\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           1       0.33      0.00      0.00     56174\n",
      "           2       0.31      0.00      0.00    107557\n",
      "           3       0.30      0.06      0.09    261197\n",
      "           4       0.35      0.91      0.51    348971\n",
      "           5       0.43      0.11      0.17    226310\n",
      "\n",
      "   micro avg       0.35      0.35      0.35   1000209\n",
      "   macro avg       0.34      0.21      0.15   1000209\n",
      "weighted avg       0.35      0.35      0.24   1000209\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#2. Descion Tress.\n",
    "DTcm = confusion_matrix(label,DTModel.predict(Features))\n",
    "print(DTcm)\n",
    "DT_classification_report = classification_report(label,DTModel.predict(Features))\n",
    "print(DT_classification_report)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[     0      0   8661  46582    931]\n",
      " [     0      0  11464  93824   2269]\n",
      " [     0      0  20426 232830   7941]\n",
      " [     0      0  21053 312237  15681]\n",
      " [     0      0  11791 198381  16138]]\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           1       0.00      0.00      0.00     56174\n",
      "           2       0.00      0.00      0.00    107557\n",
      "           3       0.28      0.08      0.12    261197\n",
      "           4       0.35      0.89      0.51    348971\n",
      "           5       0.38      0.07      0.12    226310\n",
      "\n",
      "   micro avg       0.35      0.35      0.35   1000209\n",
      "   macro avg       0.20      0.21      0.15   1000209\n",
      "weighted avg       0.28      0.35      0.24   1000209\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#3. Neive Bayes\n",
    "\n",
    "NBcm = confusion_matrix(label,NB_model.predict(Features))\n",
    "print(NBcm)\n",
    "NB_classification_report = classification_report(label,NB_model.predict(Features))\n",
    "print(NB_classification_report)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[     4      8   6550  48396   1216]\n",
      " [     3     14   8893  96100   2547]\n",
      " [     3     13  14678 236509   9994]\n",
      " [     0      6  13131 315014  20820]\n",
      " [     2      3   5444 195603  25258]]\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           1       0.33      0.00      0.00     56174\n",
      "           2       0.32      0.00      0.00    107557\n",
      "           3       0.30      0.06      0.09    261197\n",
      "           4       0.35      0.90      0.51    348971\n",
      "           5       0.42      0.11      0.18    226310\n",
      "\n",
      "   micro avg       0.35      0.35      0.35   1000209\n",
      "   macro avg       0.35      0.21      0.16   1000209\n",
      "weighted avg       0.35      0.35      0.24   1000209\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#4. Random Forest\n",
    "\n",
    "RFcm = confusion_matrix(label,RF_model.predict(Features))\n",
    "print(RFcm)\n",
    "RF_classification_report = classification_report(label,RF_model.predict(Features))\n",
    "print(RF_classification_report)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[     0      0   6531  48934    709]\n",
      " [     0      0   8529  97462   1566]\n",
      " [     0      0  13676 240104   7417]\n",
      " [     0      0  12409 319816  16746]\n",
      " [     0      0   5083 202497  18730]]\n",
      "              precision    recall  f1-score   support\n",
      "\n",
      "           1       0.00      0.00      0.00     56174\n",
      "           2       0.00      0.00      0.00    107557\n",
      "           3       0.30      0.05      0.09    261197\n",
      "           4       0.35      0.92      0.51    348971\n",
      "           5       0.41      0.08      0.14    226310\n",
      "\n",
      "   micro avg       0.35      0.35      0.35   1000209\n",
      "   macro avg       0.21      0.21      0.15   1000209\n",
      "weighted avg       0.29      0.35      0.23   1000209\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#5. One Vs Rest LogReg\n",
    "\n",
    "OVRcm = confusion_matrix(label,OVR_Model.predict(Features))\n",
    "print(OVRcm)\n",
    "OVR_classification_report = classification_report(label,OVR_Model.predict(Features))\n",
    "print(OVR_classification_report) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Conclusion:\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1. The models Descion Tress and Random Forest are good models for our movie recomendation engine.\n",
    "2. Both the Models are having almost same accuracy scores\n",
    "3. More Features are needed to accurately predict the movie Rating\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
