# API Reliability Monitor — SLA Report

> Last updated: **2026-07-13 01:09 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **5/12** &nbsp;|&nbsp; Avg uptime: **78.5%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 80.93% | 2106.1 | 10206.7 | 1000ms | 267/1400 |
| ❌ | `public_apis_list` | 0.0% | 99.71% | 122.4 | 4595.4 | 1500ms | 4/1400 |
| ❌ | `ipapi_check` | 74.86% | 99.93% | 154.1 | 4507.0 | 2500ms | 1/1400 |
| ❌ | `nasa_apod` | 75.21% | 50.86% | 3265.0 | 11152.5 | 2000ms | 688/1400 |
| ❌ | `dog_ceo_random` | 94.79% | 96.57% | 544.2 | 10244.1 | 2500ms | 48/1400 |
| ⚠️ | `open_meteo_weather` | 98.64% | 97.07% | 725.4 | 14877.1 | 2000ms | 41/1400 |
| ⚠️ | `rest_countries` | 98.93% | 98.64% | 311.6 | 10221.5 | 2500ms | 19/1400 |
| ✅ | `useless_fact` | 99.64% | 99.71% | 634.1 | 10229.6 | 2500ms | 4/1400 |
| ✅ | `catfact_random` | 99.79% | 99.36% | 255.9 | 10080.2 | 3000ms | 9/1400 |
| ✅ | `coingecko_bitcoin` | 99.79% | 99.93% | 97.7 | 4328.4 | 1500ms | 1/1400 |
| ✅ | `agify_name` | 99.93% | 99.71% | 385.4 | 16112.2 | 2000ms | 4/1400 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.86% | 209.5 | 3882.8 | 2000ms | 2/1400 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 02:00 | 5333.5 | 66.67% |
| `nasa_apod` | 03:00 | 4597.2 | 77.27% |
| `nasa_apod` | 09:00 | 4062.5 | 53.33% |
| `nasa_apod` | 05:00 | 4062.2 | 58.97% |
| `nasa_apod` | 17:00 | 4055.0 | 54.79% |
| `numbers_trivia` | 03:00 | 3835.9 | 36.36% |
| `nasa_apod` | 01:00 | 3828.5 | 55.81% |
| `nasa_apod` | 18:00 | 3664.0 | 51.35% |
| `nasa_apod` | 12:00 | 3605.8 | 53.23% |
| `nasa_apod` | 11:00 | 3490.3 | 51.95% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
