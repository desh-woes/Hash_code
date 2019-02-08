from random import randint, choice, choices, sample
from itertools import product


# To use this, simply call
# gen_youtube_problem(file name goes here)
# or
# gen_wifi_problem(file name goes here)
# at the end of the file

# Small helper to create one line describing a row in the wifi problem
# The idea is to pick column_width characters, favoring the '-'
def gen_line(width):
    opts = ['#', '-', '.']
    return ''.join(choices(population=opts, weights=[0.3, 0.5, 0.2], k=width))


# Provide a file name, and this will generate a file that follows the format of the wifi problem
# problem url: https://storage.googleapis.com/coding-competitions.appspot.com/HC/2017/hashcode2017_final_task.pdf
def gen_wifi_problem(fileName):
    output = open(fileName, 'w')

    # Random variables as per instructions, number were brought down a bit
    row_count = randint(1, 100)
    column_count = randint(1, 100)
    router_radius = randint(1, 10)

    backbone_price = randint(1, 5)
    router_price = randint(5, 100)

    budget = 10**randint(0, 9)

    # The backbone should be in some valid position
    backbone_origin = (randint(0, row_count-1), randint(0, column_count - 1))

    # The first 3 lines are straightforward. I'm starting with newlines to avoid
    # headaches in the loop below
    output.write("{0} {1} {2}".format(row_count, column_count, router_radius))
    output.write("\n{0} {1} {2}".format(backbone_price, router_price, budget))
    output.write("\n{0} {1}".format(backbone_origin[0], backbone_origin[1]))

    # Now we describe the building/area to put wifi in.
    # Each row is generated by our helper function
    for i in range(row_count):
        output.write('\n' + gen_line(column_count))

# Provide a file name, and this will generate a file that follows the format of the youtube problem
# problem url: https://storage.googleapis.com/coding-competitions.appspot.com/HC/2017/hashcode2017_qualification_task.pdf
def gen_youtube_problem(fileName):
    output = open(fileName, 'w')

    # Random variables as per instructions, number were brought down a bit
    video_count = randint(1, 20)
    endpoint_count = randint(1, 20)
    descriptions_count = randint(1, 100)
    cache_count = randint(1, 10)
    cache_capacity = randint(1, 5000)

    # First line is straightforward
    output.write("{0} {1} {2} {3} {4}".format(video_count, endpoint_count, descriptions_count,
                                                cache_count, cache_capacity))

    # The madness begins. The next line should have a size for each video, separated by a space.
    # join is a string method that connects all elements of a list of strings using the string it is called on
    # In this case, it will connect everything in the list generated using a space
    video_sizes = ' '.join((str(randint(1, 1000)) for i in range(video_count)))
    output.write("\n" + video_sizes)

    # Now for each endpoint:
    for i in range(endpoint_count):
        # how many caches is this endpoint connected to?
        endpoint_cache_count = randint(0, cache_count)
        datacenter_latency = randint(100, 1500)
        output.write("\n{0} {1}".format(datacenter_latency, endpoint_cache_count))

        # Now we need to provide latencies for each of the specific caches this endpoint is connected to
        # get a set of cache ids
        cache_set = set(range(cache_count))
        # pick #endpoint_cache_count ids, this does not replace them so they will all be unique.
        caches = sample(cache_set, endpoint_cache_count)

        # For each cache, write to the file a random latency.
        for cache in caches:
            endpoint_latency = randint(10, 1000)
            output.write("\n{0} {1}".format(cache, endpoint_latency))

    # Same idea for the descriptions. These describe some number of requests for a video from an endpoint
    # We first figure out all possible pairings using the product of the 2 sets: video ids and endpoint ids
    video_endpoint_pairs = set(product(range(video_count), range(endpoint_count)))
    # We then sample #descriptions_count of them
    pairs = sample(video_endpoint_pairs, descriptions_count)
    # for each pair(video_id, endpoint_id) get a random request count and write
    for pair in pairs:
        request_count = randint(10, 10000)
        output.write("\n{0} {1} {2}".format(pair[0], pair[1], request_count))
