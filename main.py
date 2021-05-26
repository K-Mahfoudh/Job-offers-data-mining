from careerjet_api_client import CareerjetAPIClient
import pandas as pd
import argparse
import urllib


# Function to make api call
def make_request(page, args):
    url = add_url_params(args)
    cj = CareerjetAPIClient("en_US");
    result_json = cj.search({
        'location': args.location,
        'affid': args.aff_id,
        'user_ip': args.user_ip,
        'pagesize': args.page_size,
        'keywords': args.keywords,
        'page': page,
        'url': url,
        'user_agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
    });
    return result_json['pages'], result_json


# searching jobs available by loction and keywords
def request_jobs(args):
    # Getting total pages number
    if (not args.pages):
        pages, _ = make_request(1, args)
    else:
        pages = args.pages

    # getting jobs in each page
    job_list = []
    for page_number in range(pages):
        _, result_json = make_request(page_number, args)
        for job in result_json["jobs"]:
            job_list.append(job)

    # Converting list of jobs to dataframe
    df = pd.DataFrame(job_list)
    df.to_csv(args.csv_destination)


# A function that take keywords, and converts it into url parameters
def add_url_params(args):
    param_dict = {}
    param_dict["s"] = args.keywords
    param_dict["l"] = args.location
    url = args.api_url + '?' + urllib.parse.urlencode(param_dict)
    print(url)
    return url


# Main function
def main():
    parser = argparse.ArgumentParser(description='Controling search keywords and parameters')
    parser.add_argument(
        '-k', '--keywords', required=False, type=str, help='keywords used in searching', default="python automation")
    parser.add_argument(
        '-p', '--pages', required=False, type=int, help='Number of pages')
    parser.add_argument(
        '-ps', '--page_size', required=False, type=int, help='size of jobs to be extracted on each request', default=99)
    parser.add_argument(
        '-l', '--location', required=False, type=str, help='location of searched jobs', default="New York City, NY")
    parser.add_argument(
        '-ai', '--aff_id', required=False, type=str, help='API id provided by careetjet', default="213e213hd12344552")
    parser.add_argument(
        '-i', '--user_ip', required=False, type=str, help="user's ip", default="11.22.33.44")
    parser.add_argument(
        '-u', '--api_url', required=False, type=str,
        help="url of the request, can be found when doing a search in careerjet",
        default="https://www.careerjet.com/search/jobs")
    parser.add_argument(
        '-c', '--csv_destination', required=False, type=str, help="user's ip", default="jobs_list.csv")

    # Getting command line arguments
    args = parser.parse_args()

    # searching jobs
    request_jobs(args)

    return 0


if __name__ == '__main__':
    main()
