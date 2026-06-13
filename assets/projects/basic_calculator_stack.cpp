#include <iostream>
#include <stack>
#include <string>
using namespace std;

int calculate(string s) {
    stack<int> st;

    int result = 0;
    int number = 0;
    int sign = 1;

    for (int i = 0; i < s.length(); i++) {
        char ch = s[i];

        if (ch >= '0' && ch <= '9') {
            number = 0;

            while (i < s.length() && s[i] >= '0' && s[i] <= '9') {
                number = number * 10 + (s[i] - '0');
                i++;
            }

            result += sign * number;
            i--;
        }
        else if (ch == '+') {
            sign = 1;
        }
        else if (ch == '-') {
            sign = -1;
        }
        else if (ch == '(') {
            st.push(result);
            st.push(sign);

            result = 0;
            sign = 1;
        }
        else if (ch == ')') {
            int oldSign = st.top();
            st.pop();

            int oldResult = st.top();
            st.pop();

            result = oldResult + oldSign * result;
        }
    }

    return result;
}

int main() {
    string s;

    cout << "Enter expression: ";
    getline(cin, s);

    cout << "Result = " << calculate(s) << endl;

    return 0;
}
