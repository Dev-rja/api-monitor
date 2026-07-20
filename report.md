# API Reliability Monitor — SLA Report

> Last updated: **2026-07-20 07:54 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **78.4%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 82.31% | 1972.2 | 10206.7 | 1000ms | 267/1509 |
| ❌ | `public_apis_list` | 0.0% | 99.73% | 122.5 | 4595.4 | 1500ms | 4/1509 |
| ❌ | `ipapi_check` | 72.5% | 99.93% | 152.4 | 4507.0 | 2500ms | 1/1509 |
| ❌ | `nasa_apod` | 76.54% | 52.42% | 3133.4 | 11152.5 | 2000ms | 718/1509 |
| ⚠️ | `dog_ceo_random` | 95.03% | 96.22% | 563.8 | 10244.1 | 2500ms | 57/1509 |
| ⚠️ | `open_meteo_weather` | 98.74% | 97.28% | 713.6 | 14877.1 | 2000ms | 41/1509 |
| ✅ | `rest_countries` | 99.01% | 98.74% | 302.9 | 10221.5 | 2500ms | 19/1509 |
| ✅ | `useless_fact` | 99.67% | 99.73% | 635.8 | 10229.6 | 2500ms | 4/1509 |
| ✅ | `catfact_random` | 99.8% | 99.4% | 255.3 | 10080.2 | 3000ms | 9/1509 |
| ✅ | `coingecko_bitcoin` | 99.8% | 99.93% | 96.7 | 4328.4 | 1500ms | 1/1509 |
| ✅ | `agify_name` | 99.93% | 99.73% | 384.8 | 16112.2 | 2000ms | 4/1509 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.87% | 205.0 | 3882.8 | 2000ms | 2/1509 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4339.2 | 75.0% |
| `nasa_apod` | 05:00 | 4220.5 | 60.0% |
| `nasa_apod` | 09:00 | 3891.8 | 50.79% |
| `nasa_apod` | 17:00 | 3842.7 | 52.56% |
| `nasa_apod` | 01:00 | 3549.1 | 51.06% |
| `numbers_trivia` | 03:00 | 3543.3 | 33.33% |
| `nasa_apod` | 11:00 | 3496.8 | 51.19% |
| `nasa_apod` | 12:00 | 3477.2 | 53.03% |
| `nasa_apod` | 18:00 | 3405.2 | 48.15% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
