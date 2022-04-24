## 1 and 2

query{
  quiz
  allQuizzes{
    id
    title
  }
  allQuestions(id:1){
    title
    #quiz
  }
  allAnswers(id:1){
    answerText
  }
}


## 2

query GetQuestion($id: Int = 1){
  quiz
  allQuizzes{
    id
    title
  }
  allQuestions(id:$id){
    title
    #quiz
  }
  allAnswers(id:$id){
    answerText
  }
}

