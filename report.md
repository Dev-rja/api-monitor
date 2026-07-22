# API Reliability Monitor — SLA Report

> Last updated: **2026-07-22 09:02 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 82.54% | 1948.1 | 10206.7 | 1000ms | 268/1535 |
| ❌ | `public_apis_list` | 0.0% | 99.74% | 122.8 | 4595.4 | 1500ms | 4/1535 |
| ❌ | `ipapi_check` | 71.66% | 99.93% | 152.1 | 4507.0 | 2500ms | 1/1535 |
| ❌ | `nasa_apod` | 76.94% | 53.22% | 3087.9 | 11152.5 | 2000ms | 718/1535 |
| ⚠️ | `dog_ceo_random` | 95.11% | 96.29% | 561.6 | 10244.1 | 2500ms | 57/1535 |
| ⚠️ | `open_meteo_weather` | 98.76% | 97.33% | 711.8 | 14877.1 | 2000ms | 41/1535 |
| ✅ | `rest_countries` | 99.02% | 98.7% | 303.3 | 10221.5 | 2500ms | 20/1535 |
| ✅ | `useless_fact` | 99.67% | 99.74% | 636.9 | 10229.6 | 2500ms | 4/1535 |
| ✅ | `catfact_random` | 99.8% | 99.41% | 255.8 | 10080.2 | 3000ms | 9/1535 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.93% | 97.0 | 4328.4 | 1500ms | 1/1535 |
| ✅ | `agify_name` | 99.93% | 99.74% | 385.7 | 16112.2 | 2000ms | 4/1535 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 203.8 | 3882.8 | 2000ms | 2/1535 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 03:00 | 4182.2 | 72.0% |
| `nasa_apod` | 17:00 | 3842.7 | 52.56% |
| `nasa_apod` | 09:00 | 3789.7 | 49.23% |
| `nasa_apod` | 01:00 | 3487.7 | 50.0% |
| `nasa_apod` | 12:00 | 3477.2 | 53.03% |
| `nasa_apod` | 11:00 | 3458.1 | 50.59% |
| `numbers_trivia` | 03:00 | 3417.3 | 32.0% |
| `nasa_apod` | 18:00 | 3331.3 | 46.99% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
